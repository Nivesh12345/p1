var canvas = document.querySelector("canvas");
let width = (canvas.width = window.innerWidth);
let height = (canvas.height = window.innerHeight);
let ctx = canvas.getContext("2d");

// let mouse = { x: width / 2, y: height / 2 };
let mouse = { x: 0, y: height / 2 };
let mouseRadius = 100; // Distance to the first segment
let segmentLength = 1; // Length of each segment
let numSegments = 2100; // Total number of segments

// Initialize the rope as an array of points
let rope = [];
for (let i = 0; i < numSegments; i++) {
  rope.push({ x: mouse.x + i * segmentLength, y: mouse.y });
}

// Update canvas size on window resize
window.addEventListener("resize", () => {
  width = canvas.width = window.innerWidth;
  height = canvas.height = window.innerHeight;
});

// Track mouse position
window.addEventListener("mousemove", (event) => {
  mouse.x = event.x;
  mouse.y = event.y;
});

// Draw a circle
function drawCircle(x, y, radius, color,cir) {
  ctx.beginPath();
  ctx.arc(x, y, radius, 0, Math.PI * 2);
  if (cir){
    ctx.fillStyle = color;
    ctx.fill();

  }else{

    ctx.strokeStyle = color;
    ctx.stroke();
  }
}

// Calculate the distance between two points
function calculateDistance(p1, p2) {
  return Math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2);
}

// Apply a constraint between two points
function applyConstraint(p1, p2, fixedDistance) {
  let distance = calculateDistance(p1, p2);
  if (distance === 0 || distance === fixedDistance) return;

  let correctionFactor = (distance - fixedDistance) / distance;
  let correctionX = (p2.x - p1.x) * correctionFactor;
  let correctionY = (p2.y - p1.y) * correctionFactor;

  // Move the second point closer to the first
  p2.x -= correctionX;
  p2.y -= correctionY;
}
size = 0;
// Apply the FABRIK algorithm
function fabrik() {
  // Forward pass: Start from the mouse position
  rope[0] = { x: mouse.x, y: mouse.y }; // First segment follows the mouse
  for (let i = 1; i < rope.length; i++) {
    applyConstraint(rope[i - 1], rope[i], segmentLength);
  }

  // Backward pass: Anchor the last segment in place
  // let ball = { x: width / 2, y: height / 2 }; // Ball's position
  // rope[rope.length - 1] = ball;

  // for (let i = rope.length - 2; i >= 0; i--) {
  //   applyConstraint(rope[i + 1], rope[i], segmentLength);
  // }
}
particles =[];
// Animation loop
hue = 0;
function animate() {
  requestAnimationFrame(animate);
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  
  // Apply FABRIK algorithm
  fabrik();
  
  // Draw the rope segments
  for (let i = 0; i < rope.length; i++) {
    color = 'hsl(' + hue + ',100%,50%)';
    // drawCircle(rope[i].x, rope[i].y, 20+size, i === 0 ? "red" : "blue");
    drawCircle(rope[i].x, rope[i].y, size, color,1);
    hue = (hue+1)%360;
    // hue = (hue+1)%360;
    
    // size-=1;
    size = mouseRadius * (1 - i / rope.length); // Gradually shrink the size
    if (i > 0) {
        ctx.beginPath();
        ctx.moveTo(rope[i - 1].x, rope[i - 1].y);
        ctx.lineTo(rope[i].x, rope[i].y);
        // ctx.strokeStyle = "blue";
        ctx.strokeStyle = color;
        ctx.stroke();
      }
    }
    // Draw the ball
    // drawCircle(width / 2, height / 2, 15, "green");
    hue = (hue+50)%360;
    // hue = (hue+50)%360;
    // hue = (hue+70)%360;
    //after 70 it just incrase the speed the color moving
    // hue = (hue+190)%360;
    // hue = (hue+3000)%360;
  size = 10;
  // color = 'hsl(' + hue + ',100%,50%)';
  // particles.push(drawCircle(mouse.x,mouse.y,10,color));
  // for(let i =0; i < particles.length; i++){
  //   particles[i].draw();
  // }
  // hue += (hue+30)%360;
}

// Start the animation loop
animate();
