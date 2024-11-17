var canvas = document.querySelector("canvas");

let width = canvas.width = window.innerWidth;
let height = canvas.height = window.innerHeight;
let ctx = canvas.getContext("2d");
let mouse = { x: undefined, y: undefined };
let mouseRadius = 100;  // Initial mouse radius

// Track mouse position
window.addEventListener("mousemove", function(event) {
    mouse.x = event.x;
    mouse.y = event.y;
    console.log(mouse);
});

// Event listener for keydown to increase or decrease the mouse radius
window.addEventListener("keydown", function(event) {
    if (event.key === "ArrowUp") {
        mouseRadius += 1;  // Increase mouse radius by 1
    } else if (event.key === "ArrowDown") {
        mouseRadius = Math.max(1, mouseRadius - 1);  // Decrease mouse radius by 1, prevent going below 1
    }
});

// Resize event to regenerate particles on window resize
window.addEventListener("resize", function() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
    particles = [];  // Clear particles array
    createParticles();  // Regenerate particles
});

class Particle {
    constructor(x, y) {
        this.x = x;  // Set x position
        this.y = y;  // Set y position
        this.radius = 5;
        this.minradius = 1;
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
        ctx.fillStyle = "white";
        ctx.fill();
    }

    update() {
        this.draw();

        // Calculate the distance between the particle and the mouse
        var dist = Math.sqrt(Math.pow(mouse.x - this.x, 2) + Math.pow(mouse.y - this.y, 2));

        // Check if mouse is within a certain distance of the particle
        if (dist < this.radius + mouseRadius) {  // Use global mouseRadius
            if (this.radius > this.minradius) {
                this.radius -= 0.5;  // Decrease the radius when the mouse is near
            }
        } else if (this.radius < 5) {  // Max radius
            this.radius += 0.1;  // Increase the radius when the mouse is away
        }
    }
}

// Particle creation logic
var particles = [];
function createParticles() {
    for (let i = 10; i < width; i += 20) {
        for (let j = 10; j < height; j += 20) {
            particles.push(new Particle(i, j));  // Create particles at specific grid positions
        }
    }
}

createParticles();  // Initial particle generation

function animate() {
    requestAnimationFrame(animate);

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    particles.forEach(particle => {
        particle.update();
    });
}

animate();
