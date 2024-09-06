document.addEventListener('DOMContentLoaded', () => {
    const bookmarkButton = document.getElementById('b1');

    // Herb data to store (you can replace this data with dynamic values)
    const herbData = {
        name: 'Ginger',
        scientificName: 'Zingiber officinale',
        image: 'images/image1.jpg',
        description: 'Ginger is a flowering plant whose rhizome, commonly known as ginger root, is widely used as a spice and traditional medicine.',
        id: 1,
        link: 'ginger.html'
    };

    // Check if already bookmarked
    const bookmarks = JSON.parse(localStorage.getItem('bookmarks')) || [];
    const isBookmarked = bookmarks.some(item => item.id === herbData.id);

    // If already bookmarked, change the button text to "Go to Bookmarks"
    if (isBookmarked) {
        bookmarkButton.innerHTML = '<i class="fa-solid fa-bookmark"></i>&nbsp;&nbsp;Go to Bookmarks';
    }

    // Add click event listener to the bookmark button
    bookmarkButton.addEventListener('click', () => {
        if (!isBookmarked) {
            // Store herb data in localStorage
            bookmarks.push(herbData);
            localStorage.setItem('bookmarks', JSON.stringify(bookmarks));

            // Change button text to "Go to Bookmarks"
            bookmarkButton.innerHTML = '<i class="fa-solid fa-bookmark"></i>&nbsp;&nbsp;Go to Bookmarks';
            window.location.reload();
        } else {
            // Redirect to bookmarks page (you can replace this with the actual link to the bookmarks page)
            window.location.href = 'cart.html'; // Update this URL as per your bookmark page
        }
    });
});
