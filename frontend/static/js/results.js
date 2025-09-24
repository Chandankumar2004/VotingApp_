document.addEventListener('DOMContentLoaded', () => {
    const socket = io();

    const bjpCount = document.getElementById('bjp-count');
    const rjdCount = document.getElementById('rjd-count');
    const congressCount = document.getElementById('congress-count');
    const viewDetailsBtn = document.getElementById('view-details-btn');
    const detailedVotesDiv = document.getElementById('detailed-votes');
    const voteTableBody = document.querySelector('#vote-table tbody');
    const resetVotesBtn = document.getElementById('reset-votes-btn');

    const resultItems = {
        'BJP': document.getElementById('bjp-result'),
        'RJD': document.getElementById('rjd-result'),
        'Congress': document.getElementById('congress-result'),
    };

    let selectedPartyForDetails = null;

    // Add click listeners to result items
    for (const party in resultItems) {
        resultItems[party].addEventListener('click', () => {
            selectedPartyForDetails = party;
            // Highlight the clicked item
            for (const p in resultItems) {
                resultItems[p].classList.remove('selected-for-details');
            }
            resultItems[party].classList.add('selected-for-details');
            // If detailed votes are visible, update them for the selected party
            if (detailedVotesDiv.style.display === 'block') {
                fetchAndDisplayDetailedVotes(selectedPartyForDetails);
            }
        });
    }

    // Auto-refresh results every 3 seconds
    setInterval(fetchResults, 3000);

    // Initial fetch of results
    fetchResults();

    async function fetchResults() {
        try {
            const response = await fetch('/get_results');
            const data = await response.json();
            updateResults(data);
        } catch (error) {
            console.error('Error fetching results:', error);
        }
    }

    function updateResults(data) {
        bjpCount.textContent = data['BJP'] || 0;
        rjdCount.textContent = data['RJD'] || 0;
        congressCount.textContent = data['Congress'] || 0;

        // Collect party data for sorting
        const partyData = [];
        for (const party in data) {
            partyData.push({ name: party, votes: data[party] || 0 });
        }

        // Sort parties by votes in descending order
        partyData.sort((a, b) => b.votes - a.votes);

        // Get the container for results
        const resultsDisplay = document.getElementById('results-display');

        // Reorder result items in the DOM
        partyData.forEach(party => {
            const item = resultItems[party.name];
            if (item) {
                resultsDisplay.appendChild(item);
            }
        });

        // Celebration logic
        let maxVotes = 0;
        let winner = null;

        for (const option in data) {
            if (data[option] > maxVotes) {
                maxVotes = data[option];
                winner = option;
            }
        }

        // Remove 'winner' class from all items first
        for (const option in resultItems) {
            resultItems[option].classList.remove('winner');
        }

        // Add 'winner' class to the winning item(s)
        if (winner !== null && maxVotes > 0) {
            for (const option in data) {
                if (data[option] === maxVotes) {
                    resultItems[option].classList.add('winner');
                }
            }
        }
    }

    viewDetailsBtn.addEventListener('click', () => {
        if (detailedVotesDiv.style.display === 'none') {
            // If hidden, show all details
            detailedVotesDiv.style.display = 'block';
            viewDetailsBtn.textContent = 'Hide Detailed Votes';
            // Fetch all detailed votes initially, or filtered if a party was already selected
            fetchAndDisplayDetailedVotes(selectedPartyForDetails);
        } else {
            // If visible, hide it
            detailedVotesDiv.style.display = 'none';
            viewDetailsBtn.textContent = 'View Detailed Votes';
            selectedPartyForDetails = null; // Reset selected party
            for (const p in resultItems) {
                resultItems[p].classList.remove('selected-for-details');
            }
            voteTableBody.innerHTML = ''; // Clear table when hidden
        }
    });

    async function fetchAndDisplayDetailedVotes(party = null) {
        try {
            const response = await fetch('/get_detailed_votes');
            const detailedVotes = await response.json();

            voteTableBody.innerHTML = ''; // Clear previous table rows
            const filteredVotes = party ? detailedVotes.filter(vote => vote.choice === party) : detailedVotes;

            if (filteredVotes.length > 0) {
                filteredVotes.forEach(vote => {
                    const row = voteTableBody.insertRow();
                    const dateTime = new Date(vote.created_at);
                    const date = dateTime.toLocaleDateString();
                    const time = dateTime.toLocaleTimeString();

                    row.insertCell().textContent = vote.username;
                    row.insertCell().textContent = vote.choice;
                    row.insertCell().textContent = date;
                    row.insertCell().textContent = time;
                });
            } else {
                const row = voteTableBody.insertRow();
                const cell = row.insertCell();
                cell.colSpan = 4; // Span across all 4 columns (Date, Time, Name, Party Name)
                cell.textContent = party ? `No votes for ${party} yet.` : 'No detailed votes available yet.';
            }
        } catch (error) {
            console.error('Error fetching detailed votes:', error);
            voteTableBody.innerHTML = '<tr><td colspan="4">Error loading detailed votes.</td></tr>';
        }
    }

    resetVotesBtn.addEventListener('click', async () => {
        if (confirm('Are you sure you want to reset all votes? This action cannot be undone.')) {
            try {
                const response = await fetch('/reset_votes', {
                    method: 'POST',
                });
                const data = await response.json();
                if (data.success) {
                    alert(data.message);
                    fetchResults(); // Refresh main results
                    if (detailedVotesDiv.style.display === 'block') {
                        fetchAndDisplayDetailedVotes(selectedPartyForDetails); // Refresh detailed results if visible
                    }
                } else {
                    alert(`Error: ${data.message}`);
                }
            } catch (error) {
                console.error('Error resetting votes:', error);
                alert('An error occurred while resetting votes.');
            }
        }
    });


});