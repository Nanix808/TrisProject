<template>
    <div class="close">
        <div></div>
    </div>
</template>    

<style>

.close{
    height: 36px;
    width: 36px;
    background-color: white;
    box-sizing: border-box;
    box-shadow: 0 25px 25px rgba(0, 0, 0, .1);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer
  }
  .close div{
    background: url(@/assets/image/close.svg);
    background-size: contain;
    height: 25px;
    width: 25px;
  }

  .close div:hover{
    background: url(@/assets/image/close-hover.svg);
    background-size: contain;
  }

</style>