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
.left {
    float: left;
    width: 25%;
}

.right {
    float: left;
    width: 75%;
    background: rgba(#15171b, 1);
    padding: 2rem 1rem;

}

</style>

<script>

</script>


<section class="main">
    <section class="wrapper">
        <div class="left">
            <slot name="left"></slot>
        </div>
        <div class="right">
            <slot name="right"></slot>
        </div>
    </section>
</section>