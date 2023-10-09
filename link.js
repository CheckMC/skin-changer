var colorPicker = new iro.ColorPicker('#picker', {
    // Set the size of the color picker
    width: 320,
    // Set the initial color
    color: "#f00"
});

colorPicker.on('color:change', function(color) {
    // Get the selected color in HEX format
    var selectedColor = color.hexString;

    // Send the selected color to the server
    fetch('/receive_color', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ color: selectedColor })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);  // Log the response from the server
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

import * as skinview3d from "skinview3d";
const element = document.getElementById("canvas");

const viewer = new skinview3d.SkinViewer({
  canvas: element,
  width: 300,
  height: 400,
  skin: "generatedSkin_.png",
  enableControls: true
});
