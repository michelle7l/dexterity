alert("hi");

function setup() {
	createCanvas(200,200);
	background(0);

}
function(){
	var dropzone =document.getElementById('dropzone');

	dropzone.ondrop = function(e){
		e.preventDefault();

	};
	dropzone.ondragover = function(){
		this.className = 'dropzone dragover'
		return false;
	};

	dropzone.ondragleave = function(){
		this.className = 'dropzone'
		return false;
	};
}