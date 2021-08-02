function listenerFunction(ev: Event) {
    ev.preventDefault();
    console.log(ev.target.value);
    this.style.backgroundColor = "red";
}