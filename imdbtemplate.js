// ==UserScript==
// @name         IMDb Date Injector
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Displays the date from the JSON data on IMDb reference pages
// @author       You
// @match        https://www.imdb.com/title/tt*/reference/
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // JSON data (replace with your actual data)
    const movieData = [];

    // Function to extract movie title
    function getMovieTitle() {
        const heading = document.querySelector('h3[itemprop="name"]');
        const yearSpan = document.querySelector('span.titlereference-title-year');
        if (heading && yearSpan) {
            // Extract text content and remove extra spaces and year
            let title = heading.textContent.trim();
            title = title.substring(0, title.lastIndexOf('(')).trim();
            return title;
        }
        return null;
    }

    // Function to find date in JSON
    function findDateForMovie(title) {
        const movieObj = movieData.find(movie => movie.title === title);
        return movieObj? movieObj.dateRated: null;
    }

    // Function to display the date on the page
    function displayDate(date) {
        if (date) {
            const dateDiv = document.createElement('div');
            dateDiv.textContent = `Date Rated: ${date}`;
            dateDiv.style.fontWeight = 'bold'; // Style the date
            // Insert the date after the <h3> tag
            const heading = document.querySelector('h3[itemprop="name"]');
            heading.parentNode.insertBefore(dateDiv, heading.nextSibling);
        }
    }

    // Main execution
    const movieTitle = getMovieTitle();
    if (movieTitle) {
        const date = findDateForMovie(movieTitle);
        displayDate(date);
    }

})();
