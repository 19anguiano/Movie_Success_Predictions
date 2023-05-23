window.addEventListener('DOMContentLoaded', () => {
    const graphImage = document.getElementById('graphImage');
    const prevButton = document.getElementById('prevButton');
    const nextButton = document.getElementById('nextButton');
    const graphDescription = document.getElementById('graphDescription');
    const rotatingImages = document.getElementById('rotatingImages').children;
    let currentImageIndex = 0;
  
    const images = [
      'genre_distribution.png',
      'popularity_vs_revenue.png',
      'Total Revenue per Month (1950-2020).png',
      'Total Revenue per Release Month (1950-2020).png'//,
      // 'Revenue of Top 10 Movies.png',
      // 'Top_10_Movies_Titles_and_Revenue.png'
    ];
  
    // Display initial graph and description
    graphImage.src = `assets/img/${images[currentImageIndex]}`;
    graphDescription.textContent = getDescription(currentImageIndex);
  
    // Button click event handlers
    prevButton.addEventListener('click', () => {
      currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
      graphImage.src = `assets/img/${images[currentImageIndex]}`;
      graphDescription.textContent = getDescription(currentImageIndex);
    });
  
    nextButton.addEventListener('click', () => {
      currentImageIndex = (currentImageIndex + 1) % images.length;
      graphImage.src = `assets/img/${images[currentImageIndex]}`;
      graphDescription.textContent = getDescription(currentImageIndex);
    });
  
    // Get description for current image
    function getDescription(index) {
      switch (index) {
        case 0:
          return 'Description for genre_distribution.png';
        case 1:
          return 'Description for popularity_vs_revenue.png';
        case 2:
          return 'Description for Total Revenue per Month (1950-2020).png';
        case 3:
          return 'Description for Total Revenue per Release Month (1950-2020).png';
        case 4:
          return '';
        case 5:
          return 'Description for Top_10_Movies_Titles_and_Revenue.png';
        default:
          return '';
      }
    }
  });
  