async function createPin() {
      const pin = document.getElementById("createPin").value;
      const res = await fetch("/api/create_pin", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ pin })
      });
      const data = await res.json();
      document.getElementById("output").innerText = data.message;
    }

    async function deposit() {
      const pin = document.getElementById("depositPin").value;
      const amount = parseInt(document.getElementById("depositAmount").value);
      const res = await fetch("/api/deposit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ pin, amount })
      });
      const data = await res.json();
      document.getElementById("output").innerText = data.message;
    }

    async function withdraw() {
      const pin = document.getElementById("withdrawPin").value;
      const amount = parseInt(document.getElementById("withdrawAmount").value);
      const res = await fetch("/api/withdraw", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ pin, amount })
      });
      const data = await res.json();
      document.getElementById("output").innerText = data.message;
    }

    async function checkBalance() {
      const pin = document.getElementById("checkPin").value;
      const res = await fetch("/api/check_balance", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ pin })
      });
      const data = await res.json();
      document.getElementById("output").innerText = data.message;
    }