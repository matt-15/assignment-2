$(document).ready(function () {
  $("select.year-select").change(function () {
    let year = $(this).children("option:selected").val();
    window.location.href = encodeURIComponent("/dashboard/report/?year="+year);
  });
});