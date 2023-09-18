document.addEventListener("DOMContentLoaded", function () {
    const baslangicTarihInput = document.getElementById("baslangıc_tarih");
    const bitisTarihInput = document.getElementById("bitiş_tarih");

    // Add an event listener to both date inputs
    baslangicTarihInput.addEventListener("change", validateDates);
    bitisTarihInput.addEventListener("change", validateDates);

    function validateDates() {
        const baslangicTarih = new Date(baslangicTarihInput.value);
        const bitisTarih = new Date(bitisTarihInput.value);

        // Check if the start date is before the end date
        if (baslangicTarih >= bitisTarih) {
            alert("Başlangıç tarihi, bitiş tarihinden önce olmalıdır.");
            baslangicTarihInput.value = "";
            bitisTarihInput.value = "";
        }
    }
});