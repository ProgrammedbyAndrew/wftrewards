<!DOCTYPE html>
<html>
<head>
    <title>World Food Trucks Reward Points Redemption</title>
    <script src="https://cdn.jsdelivr.net/npm/qrcodejs@1/qrcode.min.js"></script>
    <style>
        body { text-align: center; background-color: red; color: white; font-family: Arial, sans-serif; }
        #qrcode { margin-top: 15px; }
    </style>
</head>
<body>
    <h2>World Food Trucks</h2>
    <h3>Reward Points Redemption</h3>
    <label for="dollars">Dollars:</label>
    <input type="number" id="dollars" min="0" step="1"><br><br>
    <label for="cents">Cents:</label>
    <input type="number" id="cents" min="0" max="99" step="1"><br><br>
    <button onclick="generateQRCode()">Generate QR Rewards Code</button>
    <div id="qrcode"></div>

    <script>
        function generateQRCode() {
            var dollars = document.getElementById('dollars').value;
            var cents = document.getElementById('cents').value;
            var amount = dollars + '.' + cents;

            document.getElementById('qrcode').innerHTML = '';
            new QRCode(document.getElementById('qrcode'), amount);
        }
    </script>
</body>
</html>
