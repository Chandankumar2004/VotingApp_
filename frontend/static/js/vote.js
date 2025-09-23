document.addEventListener('DOMContentLoaded', () => {
    const voteForm = document.getElementById('vote-form');
    const messageDiv = document.getElementById('message');

    voteForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const selectedOption = document.querySelector('input[name="option"]:checked');
        if (!selectedOption) {
            messageDiv.textContent = 'Please select an option.';
            messageDiv.style.color = 'red';
            return;
        }

        const choice = selectedOption.value;

        try {
            const response = await fetch('/cast_vote', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `option=${encodeURIComponent(choice)}`,
            });

            const data = await response.json();

            if (data.success) {
                messageDiv.textContent = data.message;
                messageDiv.style.color = 'green';
                // Optionally redirect to results page or disable form
                window.location.href = '/results';
            } else {
                messageDiv.textContent = data.message;
                messageDiv.style.color = 'red';
            }
        } catch (error) {
            console.error('Error casting vote:', error);
            messageDiv.textContent = 'An error occurred. Please try again.';
            messageDiv.style.color = 'red';
        }
    });
});