document.addEventListener(
    "DOMContentLoaded",
    function () {

        const toasts =
            document.querySelectorAll(
                ".toast-message"
            );


        toasts.forEach(function (toast) {

            setTimeout(function () {

                closeToast(toast.id);

            }, 5000);

        });

        const navbar =
            document.querySelector(".navbar");

        const navToggle =
            document.querySelector(".nav-toggle");

        if (navToggle && navbar) {

            navToggle.setAttribute("aria-expanded", "false");

            navToggle.addEventListener("click", function () {

                const isOpen = navbar.classList.toggle("open");
                navToggle.setAttribute("aria-expanded", String(isOpen));

            });

            const navLinks = navbar.querySelectorAll(".nav-link");

            navLinks.forEach(function (link) {

                link.addEventListener("click", function () {

                    navbar.classList.remove("open");
                    navToggle.setAttribute("aria-expanded", "false");

                });

            });

        }

    }
);


function closeToast(toastId) {

    const toast =
        document.getElementById(toastId);

    if (!toast) {
        return;
    }


    toast.style.transition =
        "all 0.3s ease";

    toast.style.opacity = "0";

    toast.style.transform =
        "translateX(40px)";


    setTimeout(function () {

        toast.remove();

    }, 300);

}