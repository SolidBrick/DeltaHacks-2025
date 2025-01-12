<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Company Ranking</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        #ranking-list { list-style: none; padding: 0; }
        li { background: #f4f4f4; padding: 10px; margin: 5px; border-radius: 5px; }
        input, button { padding: 10px; margin: 10px; }
    </style>
</head>
<body>

    <h2>Enter a Company to Get Its Ranking</h2>
    
    <!-- Input for company name -->
    <input type="text" id="company-input" placeholder="Enter company name">
    <button onclick="addCompanyRanking()">Submit</button>

    <h3>Rankings</h3>
    <ul id="ranking-list"></ul>
    
    <script>
        let rankings = []; // Store company rankings

        function addCompanyRanking() {
            const inputField = document.getElementById("company-input");
            const companyName = inputField.value.trim(); // Get input value
            
            if (companyName === "") {
                alert("Please enter a company name.");
                return;
            }

             // Generate a random ranking score (or use a real API score)
            const score = Math.floor(Math.random() * 100) + 1;
            
            // Add to rankings array
            rankings.push({ company: companyName, score });

            // Sort rankings in descending order (higher score = better rank)
            rankings.sort((a, b) => b.score - a.score);

            // Clear input field
            inputField.value = "";

            // Update the displayed rankings
            updateRankingList();
        }

        function updateRankingList() {
            const rankingList = document.getElementById("ranking-list");
            rankingList.innerHTML = ""; // Clear existing list

            rankings.forEach((rank, index) => {
                const listItem = document.createElement("li");
                listItem.textContent = `#${index + 1} - ${rank.company} (${rank.score} points)`;
                rankingList.appendChild(listItem);
            });
        }
    </script>

</body>
</html>