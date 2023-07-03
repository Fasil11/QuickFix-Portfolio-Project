from flask import render_template, request
from flask_login import current_user, login_required
from main import app
from models import ServiceProvider, ServiceRequest

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/service_providers')
@login_required
def service_providers():
    providers = ServiceProvider.query.all()
    return render_template('service_providers.html', providers=providers)

@app.route('/service_provider/<int:provider_id>')
@login_required
def service_provider_profile(provider_id):
    provider = ServiceProvider.query.get_or_404(provider_id)
    return render_template('service_provider_profile.html', provider=provider)

@app.route('/service_requests')
@login_required
def service_requests():
    requests = ServiceRequest.query.filter_by(requested_by=current_user.id).all()
    return render_template('service_requests.html', requests=requests)

@app.route('/rating/<int:request_id>', methods=['GET', 'POST'])
@login_required
def rating(request_id):
    request = ServiceRequest.query.get_or_404(request_id)

    if request.provider_id != current_user.id:
        return redirect(url_for('service_requests'))

    if request.provider_id is None:
        return redirect(url_for('service_requests'))

    if request.provider_id is not None and request.rating is not None:
        return redirect(url_for('service_requests'))

    if request.method == 'POST':
        rating = request.form['rating']
        request.rating = rating
        db.session.commit()
        return redirect(url_for('service_requests'))

    return render_template('rating.html', request=request)