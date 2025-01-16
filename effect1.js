let canvas = document.querySelector("canvas");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let ctx = canvas.getContext("2d");
let particle = [];
let hue = 0;

window.addEventListener("resize",function(){
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    

});
let mouse = {
    x:undefined,
    y:undefined
}

// canvas.addEventListener("click",function(event){
//     mouse.x = event.x;
//     mouse.y = event.y;
//     for(let i =0;i<500;i++){
//         particle.push(new Particle());

//     }
    
    
// });
canvas.addEventListener("mousemove",function(event){
    mouse.x = event.x;
    mouse.y = event.y;
    for(let i =0;i<500;i++){
        particle.push(new Particle());

    }
    
    
});
function randomint(min,max) {
	return (Math.random() * (max - min + 1) + min);
}

class Particle{
    constructor(){
        this.x = mouse.x;
        this.y = mouse.y;
        this.size =randomint(10,15);
        // this.x = Math.random()*canvas.width;
        // this.y = Math.random()*canvas.height;
        this.sx = randomint(-3,3);
        this.sy = randomint(-3,3);
        this.color = 'hsl(' + hue + ',100%,50%)';

        
    }
    draw(){
        ctx.beginPath();
        ctx.fillStyle = this.color;
        ctx.arc(this.x,this.y,this.size,0,Math.PI*2);
        ctx.fill();
        ctx.closePath();

    }
    update(){
        this.draw();
        this.x +=this.sx;
        this.y +=this.sy;
        if(this.size>0.2){
            this.size-=0.08;
        }
        // if(this.x-this.size>=canvas.width || this.x+this.size<=0){
        //     this.x = mouse.x;
        // }
        // if(this.y-this.size>=canvas.height || this.y+this.size<=0){
        //     this.y = mouse.y;
        // }
        
    }
}
// function init(){
//     for(let i =0;i<500;i++){
//         particle.push(new Particle());
//     }
// }
// init();

function particlehandler(){
    // particle = [];
    for(let i =0;i<particle.length;i++){
        particle[i].update();
        // for(let j =i;j<particle.length;j++){
        //     const dx = particle[i].x - particle[j].x;       
        //     const dy = particle[i].y - particle[j].y;       
        //     const distance = Math.sqrt(dx*dx + dy*dy);
        //     if(distance<100){
        //         ctx.beginPath();
        //         ctx.strokeStyle = particle[i].color;
        //         ctx.lineWidth = particle[i].size/20;
        //         ctx.moveTo(particle[i].x,particle[i].y);
        //         ctx.lineTo(particle[j].x,particle[j].y);
        //         ctx.stroke();
        //     }
            
        // }
        
        if(particle[i].size<=0.3){
            particle.splice(i,1);
            i--;
        }

    }
    
}

function animate(){
    requestAnimationFrame(animate);
    // ctx.fillStyle ="rgba(0,0,0,1)"
    // ctx.fillRect(0,0,canvas.width,canvas.height);
    // ctx.fillStyle = "rgba(0,0,0,0.1)";
    
    // ctx.fillRect(0,0,canvas.width,canvas.height);
   
    
    ctx.clearRect(0,0,canvas.width,canvas.height);
    // ctx.rect(0, 0, width, height);
    // ctx.fillStyle = "black";
    // ctx.fill();
    // ctx.fill();
    // particle.forEach(particle=>{
    //     particle.update();

    // })
    particlehandler();
    hue+=5;
    // console.log(particle.length)
    
    
     
    
    


}

animate();
