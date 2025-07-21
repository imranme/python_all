def register():
    print("📋 Customer Registration:")

    # 1. Customer ID check (exactly 5 digits)
    cid = input("➤ Enter Customer ID (5 digits): ")
    if len(cid) != 5 or not cid.isdigit():
        print("❌ Customer ID must be exactly 5 digits.")
        return

    # 2. Name validation
    name = input("➤ Enter Full Name: ")
    if len(name.strip()) <= 2:
        print("❌ Name must be more than 2 characters.")
        return

    # 3. Email validation
    email = input("➤ Enter Email: ")
    if "@" not in email or ".com" not in email:
        print("❌ Invalid email address.")
        return

    # 4. Document check
    doc = input("➤ Document Type (NID/Passport/Driving License): ")
    if doc not in ["NID", "Passport", "Driving License"]:
        print("❌ Invalid document type.")
        return

    size = float(input("➤ File size in MB: "))
    if size > 10:
        print("❌ File size must be 10MB or less.")
        return

    ftype = input("➤ File format (pdf/jpg/png): ").lower()
    if ftype not in ["pdf", "jpg", "png"]:
        print("❌ Invalid file format.")
        return

    # 5. Phone number & OTP verification
    phone = input("➤ Enter phone number: ")
    print("📲 OTP sent (Assume: 1234)")
    otp = input("➤ Enter OTP: ")
    if otp != "1234":
        print("❌ Incorrect OTP.")
        return

    # 6. First-time discount
    first = input("➤ Is this your first registration? (yes/no): ").lower()
    if first == "yes":
        bill = float(input("➤ Enter total bill: "))
        discount = bill * 0.20
        print(f"✅ 20% Discount: {discount:.2f}")
        print(f"💰 Final Amount: {bill - discount:.2f}")

    print("🎉 Registration Successful!")

# Run the function
register()
