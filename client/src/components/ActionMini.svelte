<style lang="scss">
i {
    font-family: 'untitled-font-1';
}

.box {
    width: 40%;
    float: left;
    background: #15171b;
    padding: .5rem 1.5rem;
    margin: 10px 10px 5px 0;
    box-shadow: inset 0 0 4px  rgba(#000000, 0.8    );
    border-radius: 5px;
    transition: all .15s ease-in-out;
    text-align: center;
    opacity: .5;
    .icon {
        
    }
    .label {
        font-weight: bold;
        text-transform: uppercase;
        font-size: 0.7rem;
        opacity: .5;

    }
    
    &:hover {
        opacity: 1;
        box-shadow: inset 0 0 3px  rgba(#000000, 0.6    );

    }
}
</style>

<script>
    export let link, icon, label;
</script>
<a href="{link}">
    <div class="box">
        <div class="icon">
            <i class="icon-{icon}"></i>
        </div>
        <div class="label">
            {label}
        </div>
    </div>
</a>