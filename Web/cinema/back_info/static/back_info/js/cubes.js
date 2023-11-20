const cubes = [];

function AddCube() {
  const size = parseInt(document.getElementById("sizee").value);
  const color = document.getElementById("colore").value;

  const cube = {
    size: size,
    color: color,
    volume: Math.pow(size, 3),
  };

  cubes.push(cube);

  document.getElementById("sizee").value = "";
  document.getElementById("colore").value = "";
}

function GetCubes() {
  if (cubes.length === 0) {
    alert("Add cubes");
    return;
  }

  const colorInfo = {};

  cubes.forEach((cube) => {
    if (!colorInfo[cube.color]) {
      colorInfo[cube.color] = {
        count: 0,
        totalVolume: 0,
      };
    }

    colorInfo[cube.color].count++;
    colorInfo[cube.color].totalVolume += cube.volume;
  });

  let resultMessage = "Color counts and total volume:\n";

  for (const color in colorInfo) {
    resultMessage += `${color}: ${colorInfo[color].count} cubes, Total Volume: ${colorInfo[color].totalVolume} cubic centimeters\n`;
  }

  alert(resultMessage);
}
