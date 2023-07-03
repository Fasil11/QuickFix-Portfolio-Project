// Perform actions when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Handle rating selection
    const ratingStars = document.querySelectorAll('.rating-star');
  
    ratingStars.forEach((star) => {
      star.addEventListener('click', (event) => {
        const selectedRating = event.target.dataset.rating;
        console.log(`Selected rating: ${selectedRating}`);
        // You can perform further actions based on the selected rating
      });
    });
  
    // Handle service provider search
    const searchForm = document.querySelector('#search-form');
  
    searchForm.addEventListener('submit', (event) => {
      event.preventDefault();
      const searchInput = document.querySelector('#search-input');
      const selectedService = document.querySelector('#service-select').value;
      const selectedLocation = document.querySelector('#location-select').value;
  
      console.log(`Search query: ${searchInput.value}`);
      console.log(`Selected service: ${selectedService}`);
      console.log(`Selected location: ${selectedLocation}`);
      // You can perform further actions like making an AJAX request to search for service providers
    });
  
    // Other custom JavaScript logic can be added here
  });