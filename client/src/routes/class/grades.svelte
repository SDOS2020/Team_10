<style lang="scss">
.main {
	position: absolute;
	left: 50%;

	top: 50%;
	transform: translate(-50%, -50%);
}

.wrapper {

	width: 120vmin;
  height: 95vmin;
	background: rgba(#15171B, 1);
	
	box-shadow: 0 0 6px rgba(#000, 0.07);
	padding: 2rem 0rem 2rem 2rem;
}

h1{
	font-size: 2rem;
	text-transform: uppercase;
}
p {
    margin: 10px 0;
	opacity: .7;
}

::-webkit-input-placeholder {

  font-size: 30px;
}
::-moz-placeholder {

  font-size: 30px;
}
:-ms-input-placeholder {

  font-size: 30px;
}
::placeholder {

  font-size: 30px;
}



.btn {
  border: none;
  background-color: #000;
  padding: 10px 20px;
  font-size: 20px;
	color: #fff;
  cursor: pointer;
  display: inline-block;
	position: fixed;
	right:40px;
	bottom:570px;
}

.text-box {
	width: 96%;
	height: 100px;

}

input[type="text"] {
    font-size:20px;
}


.sidebar {
	height: 500px;
	width: 325px;

	position: fixed;
	left: 50px;
	top: 175px;
	background: rgba(#15171B, 1);
	
	box-shadow: 0 0 6px rgba(#000, 0.07);
	z-index: 1;



}

.sidebar a {
  padding: 6px 8px 40px 16px;
  text-decoration: none;
  font-size: 60px;
  color: #bbb;
  display: block;
}

.sidebar a:hover {
  color: #000;
}
* {
  box-sizing: border-box;
	}

	/* Create two unequal columns that floats next to each other */
	.column {
	  float: left;
	  padding: 10px;
	}

	.left {
	  width: 80%;
	}

	.right {
	  width: 20%;
	}

	/* Clear floats after the columns */
	.row:after {
	  content: "";
	  display: table;
	  clear: both;
	}

</style>

<svelte:head>
	<title>WebMP : Class</title>
</svelte:head>


<script>
</script>

	



<section class="main">
	<div class="wrapper">
		<div class="row">
		<div class="column left">
			<h2> Projects </h2>
		</div>
		<div class="column right">
			<h2>Grades</h2>
		</div>
		</div>


	</div>
</section>


<div class="sidebar">
	<a href="/profile">Profile</a>

	<a href="">Resources</a>
	<a href="">Project</a>
	<a href="/grades" style="color:#000;">Grades</a>


</div>
