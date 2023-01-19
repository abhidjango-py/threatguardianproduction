var myNav = document.getElementById("mynav");
window.onscroll = function () {
  if (
    document.body.scrollTop >= 550 ||
    document.documentElement.scrollTop >= 550
  ) {
    myNav.classList.add("nav-colored");
    myNav.classList.remove("nav-transparent");
  } else {
    myNav.classList.add("nav-transparent");
    myNav.classList.remove("nav-colored");
  }
};
