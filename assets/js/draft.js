/**
 * Show / Hide Box by checking an element value
 * @param {Object} param0
 * @param {HTMLElement | null} param0.determinative
 * @param {string | number | boolean} param0.conditionValue
 * @param {HTMLElement | null} param0.box
 * @param {HTMLElement | null} param0.textarea
 */
function handleToggleElement({ determinative, box, textarea, conditionValue }) {
    function hide() {
        textarea.value = "";
        box.style.display = "none";
    }

    function show() {
        box.style.display = "block";
    }

    function toggle() {
        if (determinative.value === conditionValue) {
            return show();
        }
        hide();
    }

    // toggle element in the first visit
    toggle();

    // toggle element when status changed
    determinative.addEventListener("change", toggle);
}

function handleToggleReceiveDescription() {
    handleToggleElement({
        box: document.querySelector(".field-receive_description"),
        textarea: document.getElementById("id_receive_description"),
        determinative: document.getElementById("id_receive_status"),
        conditionValue: "not-received",
    });
}

function handleToggleModifyDescription() {
    handleToggleElement({
        box: document.querySelector(".field-modify_description"),
        textarea: document.getElementById("id_modify_description"),
        determinative: document.getElementById("id_status"),
        conditionValue: "modify-amount",
    });
}

document.addEventListener("DOMContentLoaded", function () {
    handleToggleReceiveDescription();
    handleToggleModifyDescription();
});
