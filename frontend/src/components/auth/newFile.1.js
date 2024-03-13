export default (await import('vue')).defineComponent({
components: { Password },
props: {
isOpen: {
type: Boolean,
required: true,
},
email: {
type: String,
default: ''
},
},
emits: {
close: null,
register: null
},
data() {
return {
login: {
email: this.email,
password: '',
ip: '',
},

emailActive: false,
iconPasswordShow: false,
msg: [],
reg: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/
};
},
mounted() {
document.addEventListener("keydown", this.handleKeydown);
},
beforeUnmount() {
document.removeEventListener("keydown", this.handleKeydown);
},
watch: {
isOpen: {
handler(newValue) {
const elem = document.querySelector("body");
const offsetWidth = elem.offsetWidth;
if (newValue) {
elem.classList.add("modal-open");
elem.style.width = offsetWidth + 'px';
} else {
elem.classList.remove("modal-open");
elem.style.width = 'auto';
}

}
}
},
computed: {
loggedIn() {
return this.$auth.loggedIn;
},
user() {
return this.$auth.user;
},
buttonActive() {
return this.emailActive && this.login.password.length;
},
},


methods: {
async userLogin() {
try {
let response = await this.$auth.loginWith('local', { data: this.login });
if (this.$auth.loggedIn) {
this.close();
this.$store.commit('info/showModal', "Приветствуем вас - " + this.$auth.user.email);
}
} catch (err) {
console.log("Логин");
}

},
async userLogout() {
try {
const user = this.$auth.user.email;
await this.$auth.logout();
this.close();
this.$store.commit('info/showModal', "До свидания - " + user);
// if (this.$auth.loggedIn) {
//   console.log("Авторизация успешная")
//   this.close()
// } else {
//   console.log("Такого пользователя не существует")
// }
} catch (err) {
console.log("Сервер не отвечает2");
}
},
handleKeydown(e) {
if (this.isOpen && e.key === "Escape") {
this.close();
}
},
register() {
this.$emit("register");
},
passwordreset() {
this.$emit("passwordreset");
},
close() {
this.$emit("close");
},
validateEmail() {
// return (this.login.email == "")? "" : (this.reg.test(this.login.email)) ? 'has-success' : 'has-error';
if (!this.login.email.length) {
this.emailActive = false;
return '';
} else if (!this.reg.test(this.login.email)) {
this.emailActive = false;
return 'has-error';
}
this.emailActive = true;
return 'has-success';
}
},
});
