<style lang="scss">
.main {
	position: absolute;
	width: 70%;
	left: 50%;
	top:40%;
	transform: translate(-50%, -40%);
}

.wrapper {
	border-radius: 5px;
	// box-shadow: 0 0 6px rgba(#000, 0.07);
	padding: 2rem 0rem 2rem 2rem;

}

/*.column {
  float: left;
  width: 33.33%;
  padding: 10px;
  
}

 Clear floats after the columns 
.row:after {
  content: "";
  display: table;
  clear: both;
}
*/
.left {
	float: left;
	width: 33.33%;
}

.middle {
	float: left;
	width: 33.33%;
}

.right {
	float: left;
	width: 33.33%;
}


</style>

<section class="main">
    <section class="wrapper">
        <div class="left">
            <slot name="left"></slot>
        </div>
        <div class="middle">
        	<slot name="middle"></slot>
        </div>
        <div class="right">
            <slot name="right"></slot>
        </div>
    </section>
</section>