
function change(){
    document.getElementsByClassName('dimmed')[0].style.display = "block";
    document.getElementsByClassName('wrap')[0].style.display = "block";
    scrollPosition = window.pageYOffset;
    body.style.overflow = 'hidden';
    body.style.position = 'fixed';
    body.style.top = `-${scrollPosition}px`;
    body.style.width = '100%';
}

function change1(){
    document.getElementsByClassName('dimmed')[0].style.display = "none";
    document.getElementsByClassName('wrap')[0].style.display = "none";
    body.style.removeProperty('overflow');
    body.style.removeProperty('position');
    body.style.removeProperty('top');
    body.style.removeProperty('width');
    window.scrollTo(0, scrollPosition);

}

function setCursor(){
    document.getElementsByClassName('close')[0].style.cursor = "pointer";
}