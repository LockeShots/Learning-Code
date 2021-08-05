<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8" />
	<link id="favicon" rel="shortcut icon" type="image/png" href="data:image/png;base64,....==" />
	<style>
		html, body {
			margin: 0;
			height: 100%;
			overflow: hidden;
			text-align: center;
			background-color: black;
		}
		canvas {
			image-rendering: pixelated;
			object-fit: cover;
			height: 100%; max-height: 100%;
			max-width: 100%;
		}
	</style>
</head>
<body>
	<canvas id="canvas" width="480" height="270"></canvas>
</body>
<script type="module">

	const canvas = document.getElementById('canvas');
	const context = canvas.getContext('2d');
	const w = canvas.width;
	const h = canvas.height;


	function render(c, state) {
		c.clearRect(0, 0, w, h);  // Reset the canvas to background color

		// https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D

		// Line
		c.strokeStyle = 'cyan';
		c.lineWidth = 2;
		c.beginPath();
		c.moveTo(100, 200);
		c.lineTo(100, 100);
		c.lineTo(200, 100);
		c.lineTo(150, 150);
		c.lineTo(200, 200);
		c.stroke();
	}

	// Loop
	function main(time) {
		requestAnimationFrame(main);
		render(context);
		// TODO: this is `easy mode` there is more to this for accurate timing of frames
	}

	console.log("Ready");
	render(context);  // Render once on load
	// main();  // Render in animation loop
</script>
</html>