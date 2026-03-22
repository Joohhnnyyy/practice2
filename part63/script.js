
const mouseFollower = document.querySelector(".mouse-follower");
const mouseFollower2 = document.querySelector(".outer-mouse-follower");

let x = y = 0;
addEventListener("mousemove",(e)=>{
  const {clientX, clientY} = e;
  x = clientX;
  y = clientY;
});


function animation(){
  mouseFollower.style.transform = `translate(${x}px, ${y}px)`;
  mouseFollower2.style.transform = `translate(${x}px, ${y}px)`;
  requestAnimationFrame(animation);
}
animation();
