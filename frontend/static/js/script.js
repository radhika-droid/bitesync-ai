async function getRecommendations() {
    const goal = document.getElementById("goal").value;
    const diet = document.getElementById("diet").value;
    const sortBy = document.getElementById("sort").value;
    const btn = document.getElementById("recommendBtn");

    const resultsSection = document.getElementById("results");
    const cardsContainer = document.getElementById("cards");
    const errorSection = document.getElementById("error");
    const errorMsg = document.getElementById("errorMsg");

    // Reset UI
    cardsContainer.innerHTML = "";
    resultsSection.classList.add("hidden");
    errorSection.classList.add("hidden");

    if (!goal) {
        showError("Please select a goal before fetching recommendations.");
        return;
    }

    // Loading state
    const originalText = btn.textContent;
    btn.textContent = "Loading...";
    btn.disabled = true;

    try {
        const payload = { goal: goal };
        if (diet && diet !== "all") payload.diet = diet;
        if (sortBy) payload.sort_by = sortBy;

        const response = await fetch("/api/recommend", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (!response.ok || !data.success) {
            showError(data.error || "Something went wrong. Please try again.");
            return;
        }

        if (!data.recommendations || data.recommendations.length === 0) {
            showError("No recommendations found for the selected criteria.");
            return;
        }

        renderCards(data.recommendations);
        resultsSection.classList.remove("hidden");

    } catch (err) {
        showError("Network error: unable to connect to the server.");
        console.error(err);
    } finally {
        btn.textContent = originalText;
        btn.disabled = false;
    }
}

function renderCards(items) {
    const container = document.getElementById("cards");
    container.innerHTML = "";

    items.forEach(item => {
        const card = document.createElement("div");
        card.className = "card";

        const dietClass = item.diet_type === "veg" ? "veg" : "non-veg";
        const dietLabel = item.diet_type === "veg" ? "Vegetarian" : "Non-Veg";

        card.innerHTML = `
            <h3>${escapeHtml(item.food_name)}</h3>
            <span class="badge ${dietClass}">${dietLabel}</span>
            <ul>
                <li><strong>Calories:</strong> ${item.calories} kcal</li>
                <li><strong>Protein:</strong> ${item.protein} g</li>
                <li><strong>Carbs:</strong> ${item.carbs} g</li>
                <li><strong>Fat:</strong> ${item.fat} g</li>
            </ul>
        `;
        container.appendChild(card);
    });
}

function showError(message) {
    const errorSection = document.getElementById("error");
    const errorMsg = document.getElementById("errorMsg");
    errorMsg.textContent = message;
    errorSection.classList.remove("hidden");
}

function escapeHtml(text) {
    if (typeof text !== "string") return text;
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}

