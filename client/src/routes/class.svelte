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
	background: rgba(#fff, .6);
	border-radius: 10px;
	box-shadow: 0 0 6px rgba(#000, 0.2);
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
	height: 350px;
	width: 325px;

	position: fixed;
	left: 50px;
	top: 175px;
	background: rgba(#fff, .6);
	border-radius: 10px;
	box-shadow: 0 0 6px rgba(#000, 0.2);
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

</style>

<svelte:head>
	<title>WebMP : Class</title>
</svelte:head>

<section class="main">
	<div class="wrapper">
	   <form>
        <input type="text" class="text-box" placeholder="Share something with the class!">
        <input type="submit" class="btn" value="Post">
     </form>





	</div>
</section>


<div class="sidebar">
	<a href="">Resources</a>
	<a href="">Project</a>
	<a href="">Grades</a>


</div>
