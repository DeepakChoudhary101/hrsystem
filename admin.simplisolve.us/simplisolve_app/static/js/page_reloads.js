
    // Use the 'pageshow' event to detect page navigation, including back/forward
    window.addEventListener('pageshow', function (event) {
        // Check if the page is being loaded from the bfcache (back-forward cache)
        if (event.persisted) {
            // Force a full page reload
            window.location.reload();
        }
    });

