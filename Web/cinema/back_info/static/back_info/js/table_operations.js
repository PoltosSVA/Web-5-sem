document.getElementById("generateTable").addEventListener("click", function () {
      document.getElementById("tableContainer").innerHTML = "";

      const tableSize = parseInt(document.getElementById("tableSize").value);

      if (!isNaN(tableSize) && tableSize > 0) {
          const table = document.createElement("table");

          for (let i = 0; i < tableSize; i++) {
              const row = table.insertRow(i);
              for (let j = 0; j < tableSize; j++) {
                  const cell = row.insertCell(j);
                  const randomValue = Math.floor(Math.random() * 100);
                  cell.textContent = randomValue;
              }
          }
          document.getElementById("tableContainer").appendChild(table);
      } else {
          alert("Invalid number");
      }
});

document.getElementById("transposeTable").addEventListener("click", function () {
      const table = document.querySelector("table");
      if (table) {
          const tempTableData = [];
          const rows = table.rows;

          for (let i = 0; i < rows.length; i++) {
              tempTableData[i] = [];
              for (let j = 0; j < rows[i].cells.length; j++) {
                  tempTableData[i][j] = rows[i].cells[j].textContent;
              }
          }

          document.getElementById("tableContainer").removeChild(table);

          const transposedTable = document.createElement("table");
          for (let i = 0; i < tempTableData[0].length; i++) {
              const row = transposedTable.insertRow(i);
              for (let j = 0; j < tempTableData.length; j++) {
                  const cell = row.insertCell(j);
                  cell.textContent = tempTableData[j][i];
              }
          }

          document.getElementById("tableContainer").appendChild(transposedTable);
      } else {
          alert("Create table");
      }
});

document.getElementById("tableContainer").addEventListener("click", function (event) {
    if (event.target.tagName === "TD") {
        const cell = event.target;
        const cellValue = parseInt(cell.textContent);

        if (!isNaN(cellValue)) {
            cell.classList.remove("highlight-even", "highlight-odd");

            if (cellValue % 2 === 0) {
                cell.classList.add("highlight-even");
            } else {
                cell.classList.add("highlight-odd");
            }
        }
    }
});

const tableContainer = document.getElementById("tableContainer");
const cellLimitInput = document.getElementById("cellLimit");
const clearSelectionButton = document.getElementById("clearSelection");
const addRowButton = document.getElementById("addRow");
const addColumnButton = document.getElementById("addColumn");
let selectedCells = [];

function addRow() {
    const table = tableContainer.querySelector("table");
    const newRow = document.createElement("tr");

    for (let i = 0; i < table.rows[0].cells.length; i++) {
        const newCell = document.createElement("td");
        newCell.textContent = Math.floor(Math.random() * 100) + 1;
        newRow.appendChild(newCell);
    }

    table.appendChild(newRow);
}

function addColumn() {
    const table = tableContainer.querySelector("table");
    for (let i = 0; i < table.rows.length; i++) {
        const newCell = document.createElement("td");
        newCell.textContent = Math.floor(Math.random() * 100) + 1;
        table.rows[i].appendChild(newCell);
    }
}

tableContainer.addEventListener("click", (event) => {
    const cell = event.target;
    if (cell.tagName === "TD") {
        if (cell.classList.contains("selected")) {
            cell.classList.remove("selected");
            selectedCells = selectedCells.filter(selectedCell => selectedCell !== cell);
        } else if (selectedCells.length < cellLimitInput.value) {
            const index = cell.cellIndex;
            const row = cell.parentElement;
            if (!selectedCells.some(selectedCell => selectedCell.parentElement === row && Math.abs(selectedCell.cellIndex - index) === 1)) {
                cell.classList.add("selected");
                selectedCells.push(cell);
            }
        }
    }
});

clearSelectionButton.addEventListener("click", () => {
    selectedCells.forEach(cell => cell.classList.remove("selected"));
    selectedCells = [];
});
addRowButton.addEventListener("click", () => {
    addRow();
});

addColumnButton.addEventListener("click", () => {
    addColumn();
});
