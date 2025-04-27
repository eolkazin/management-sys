document.addEventListener("DOMContentLoaded", function () {
  // Elementos
  const addProductBtn = document.getElementById("addProductBtn");
  const productForm = document.getElementById("productSection");
  const cancelBtn = document.getElementById("cancelBtn");
  const productTable = document
    .getElementById("productTable")
    .getElementsByTagName("tbody")[0];
  const productFormContent = document.getElementById("productFormContent");
  const generateReportBtn = document.getElementById("generateReportBtn");
  const reportContent = document.getElementById("reportContent");
  const inventoryReport = document.getElementById("inventoryReport");

  // Funcionalidades do Menu
  const showProducts = document.getElementById("showProducts");
  const showEntries = document.getElementById("showEntries");
  const showExits = document.getElementById("showExits");
  const showReports = document.getElementById("showReports");

  // Mostrar as seções correspondentes
  showProducts.addEventListener("click", function () {
    toggleSection("productSection");
  });

  showEntries.addEventListener("click", function () {
    toggleSection("entrySection");
  });

  showExits.addEventListener("click", function () {
    toggleSection("exitSection");
  });

  showReports.addEventListener("click", function () {
    toggleSection("reportSection");
  });

  function toggleSection(sectionId) {
    const sections = document.querySelectorAll(".content-section");
    sections.forEach((section) => section.classList.add("hidden"));

    const activeSection = document.getElementById(sectionId);
    activeSection.classList.remove("hidden");
  }

  // Adicionar Produto
  addProductBtn.addEventListener("click", function () {
    toggleSection("productSection");
  });

  cancelBtn.addEventListener("click", function () {
    toggleSection("productSection");
  });

  // Adicionar produto à tabela
  productFormContent.addEventListener("submit", function (e) {
    e.preventDefault();

    const id = document.getElementById("productID").value;
    const name = document.getElementById("productName").value;
    const description = document.getElementById("productDescription").value;
    const category = document.getElementById("productCategory").value;
    const supplier = document.getElementById("productSupplier").value;
    const unitCost = document.getElementById("productUnitCost").value;
    const salePrice = document.getElementById("productSalePrice").value;
    const quantity = document.getElementById("productQuantity").value;
    const location = document.getElementById("productLocation").value;
    const expiryDate = document.getElementById("productExpiryDate").value;
    const image = document.getElementById("productImage").files[0];

    const row = productTable.insertRow();
    row.innerHTML = `
             <td>${id}</td>
             <td>${name}</td>
             <td>${quantity}</td>
             <td>R$ ${parseFloat(salePrice).toFixed(2)}</td>
             <td>${category}</td>
             <td>${supplier}</td>
             <td>
                 <button class="btn btn-delete">Remover</button>
             </td>
         `;
    // Limpar formulário
    productFormContent.reset();
    toggleSection("productSection");
  });

  // Remover produto
  productTable.addEventListener("click", function (e) {
    if (e.target && e.target.classList.contains("btn-delete")) {
      const row = e.target.closest("tr");
      productTable.deleteRow(row.rowIndex);
    }
  });

  // Gerar relatório
  generateReportBtn.addEventListener("click", function () {
    inventoryReport.innerHTML = "Relatório gerado com sucesso!";
    reportContent.classList.remove("hidden");
  });
});
