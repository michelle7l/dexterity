
function setup() {
	createCanvas(200,200);
	background(0);

}
function drop(){
	var dropzone =document.getElementById('dropzone');
	var upload = function(files){
		var formData = new FormData(),
			xhr = new XMLHttpRequest(),

	}
	dropzone.ondrop = function(e){
		e.preventDefault();
		this.className = 'dropzone';
		upload(e.dataTransfer.files);

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