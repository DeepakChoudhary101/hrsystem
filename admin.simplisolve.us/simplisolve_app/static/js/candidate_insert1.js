var countryCodeSelect = document.getElementById('id_country_code');
    var countryNameInput = document.getElementById('id_country_name');
    var phoneNumberInput = document.getElementById('id_code');
    var resumeInput = document.getElementById('id_resume');

    var resumeError = document.getElementById('resume-error');

    countryCodeSelect.addEventListener('change', function() {
        var selectedOption = countryCodeSelect.options[countryCodeSelect.selectedIndex];
        var selectedValues = selectedOption.value.split('+');

        var selectedName = selectedValues[0];
        var selectedCode = "+" + selectedValues[1];

        countryNameInput.value = selectedName;
        phoneNumberInput.value = selectedCode;
    });

    resumeInput.addEventListener('change', function() {
        console.log(resumeInput.value);
        var allowedExtensions = ['pdf'];
        var extension = resumeInput.value.split('.').pop().toLowerCase();
        if (allowedExtensions.indexOf(extension) === -1) {
            resumeError.textContent = 'Invalid file format. Please upload a PDF file.';
            resumeInput.value = ''; // Clear the input field
        } else {
            resumeError.textContent = '';
            console.log(resumeError)
        }
    });