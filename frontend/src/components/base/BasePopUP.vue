<template>
   

   <div class="backdrop" @mousedown="close">
    <div class="popup" @mousedown.stop>
      <!-- <div class="close">
        <div></div>
      </div>   -->
      <div class="container_button_close" @mousedown="close">

        <ButtonClose />
      </div>
      
      <h3>{{props.name}}</h3>

      <slot></slot>
    </div>
  </div>
    
  </template>
  
<script setup lang="ts">
import ButtonClose from '@/components/ui/button-close.vue';
interface Props {
  name: string
}

const props = defineProps<Props>()

const emit = defineEmits<{
  (e: 'close'): void
}>()
  

function close() {

  emit('close');

}


//   import Password from 'vue-password-strength-meter'
  
  
  </script>
  
  <style>
  input:-webkit-autofill,
  input:-webkit-autofill:hover,
  input:-webkit-autofill:focus,
  input:-webkit-autofill:active {
    transition: background-color 5000s ease-in-out 0s;
  }

  .backdrop {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.3);
  z-index: 100;
}
  
  .popup {
    position: absolute;
    top: 45%;
    left: 50%;
    max-width: 480px;
    padding: 40px;
    transform: translate(-50%, -50%);
    background: white;
    box-sizing: border-box;
    box-shadow: 0 15px 25px rgba(0, 0, 0, .1);
    display: flex;
    flex-direction: column;
    width: 90%;
    border-radius: 20px;
    cursor: default;
    /*margin-right: 76px;*/
  }

  .container_button_close {
    position: absolute;
    top: -16px;
    right: -16px;
  }
  

  
  .popup h3 {
    margin: 0 0 30px;
    padding: 0;
    color: #000000;
    text-align: center;
  }
/*   
  .popup .user-box {
    position: relative;
    padding-bottom: 30px;
  }
  
  .popup .user-box input {
    width: 100%;
    padding: 10px 0 0 0;
    height: 30px;
    line-height: 30px;
    font-size: 16px;
    color: black;
    border: none;
    border-bottom: 1px solid #000000;
    outline: none;
    background: transparent;
  } */
/*   
  .popup .user-box input.has-error {
    border-bottom: 1px solid red
  }
  
  .popup .user-box input.has-success {
    border-bottom: 1px solid #4ac3ce
  }
  
  .popup span.password-control {
    position: absolute;
    top: 9px;
    right: 0;
    display: inline-block;
    width: 24px;
    height: 24px;
    background: url(../assets/image/showpassword.svg);
    background-size: cover;
    cursor: pointer;
  } */
/*   
  .popup span.password-control.view {
    background: url(../assets/image/resetpassword.svg);
    background-size: cover;
  }
  
  .popup .user-box label {
    position: absolute;
    top: 0;
    left: 0;
    padding: 10px 0;
    font-size: 16px;
    color: #000000;
    pointer-events: none;
    transition: .5s;
  } */
/*   
  .popup .user-box input:focus ~ label,
  .popup .user-box input:valid ~ label {
    top: -20px;
    left: 0;
    font-size: 16px;
  }
  
  .popup .user-box input.has-error ~ label {
    top: -20px;
    left: 0;
    font-size: 16px;
  }
  
  .popup .user-box input.has-error ~ label {
    color: red;
  }
  
  .popup .user-box input.has-success ~ label {
    color: #4ac3ce;
  } */
  
  /* .popup .button-box {
    display: flex;
    align-items: center;
    flex-flow: row wrap;
    justify-content: space-between;
  
  }
  
  .backdrop {
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    z-index: 100;
  }
  
  .button-box .span-box {
    margin: 0 10px 10px 10px;
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-end;
    flex-grow: 1;
  
  
  }
  .button-box .span-password {
    margin-top: 20px;
  } */
  
  /* .button-box span {
    margin: 10px 10px 0 10px;
    flex-grow: 0;
    flex-shrink: 1;
    cursor: pointer;
  
  }
  
  .button-box span:hover {
    color: #4ac3ce;
  }
  
  .button-box button {
    margin: 0 10px 0 10px;
    cursor: pointer;
    border-radius: 5px;
    padding: 10px 25px;
    color: black;
    border: none;
    background-color: #d7dfe2;
    box-shadow: -5px -5px 10px white, 5px 5px 10px #90a4ae;
    transition: box-shadow 0.3s ease-in-out;
  } */
/*   
  .button-box button.has-success:hover {
    color: #4ac3ce;
  
  }
  
  .button-box button.has-error:hover {
    color: red;
  }
  
  .button-box button:disabled {
    box-shadow: -5px -5px 10px white, 5px 5px 10px #90a4ae,
    inset -5px -5px 10px white, inset 5px 5px 10px #90a4ae;
  }
  
  .button-box button.has-success:active {
    box-shadow: 0 -2px 10px #4ac3ce,
    0 2px 10px #4ac3ce,
    -2px 0 10px #4ac3ce,
    2px 0 10px #4ac3ce;
  }
  
  .button-box button.has-error:active {
    box-shadow: 0 -2px 10px red,
    0 2px 10px red,
    -2px 0 10px red,
    2px 0 10px red;
  }
  
  @media all and (max-width:505px) {
  
  .popup .button-box {
    flex-direction: column;
  }
  
  .button-box .span-box {
    margin-top: 10px;
    margin-bottom: 0;
    flex-direction: column;
    align-items: center;
  }
  
  } */
  </style>