document.addEventListener("DOMContentLoaded", () => {
    fetch("/api/birds")
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById("bird-list");
            data.forEach(bird => {
                let item = document.createElement("li");
                item.textContent = `${bird.Nome} - ${bird.Espécie} (${bird.Habitat})`;
                list.appendChild(item);
            });
        })
        .catch(error => console.error('Erro ao buscar dados:', error));
});