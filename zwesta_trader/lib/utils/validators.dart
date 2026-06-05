// Email validation
String? validateEmail(String? value) {
  if (value == null || value.isEmpty) {
    return 'Email is required';
  }
  final emailRegex = RegExp(
      r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$');
  if (!emailRegex.hasMatch(value)) {
    return 'Enter a valid email';
  }
  return null;
}

// Password validation (NIST-compliant)
String? validatePassword(String? value) {
  if (value == null || value.isEmpty) {
    return 'Password is required';
  }
  if (value.length < 8) {
    return 'Password must be at least 8 characters';
  }
  if (!RegExp(r'[a-z]').hasMatch(value)) {
    return 'Password must contain lowercase';
  }
  if (!RegExp(r'[A-Z]').hasMatch(value)) {
    return 'Password must contain uppercase';
  }
  if (!RegExp(r'\d').hasMatch(value)) {
    return 'Password must contain digit';
  }
  if (!RegExp(r'[!@#$%^&*]').hasMatch(value)) {
    return 'Password must contain special character (!@#\$%^&*)';
  }
  return null;
}

// Username validation
String? validateUsername(String? value) {
  if (value == null || value.isEmpty) {
    return 'Username is required';
  }
  if (value.length < 3) {
    return 'Username must be at least 3 characters';
  }
  if (value.length > 20) {
    return 'Username must not exceed 20 characters';
  }
  if (!RegExp(r'^[a-zA-Z0-9_.-]+$').hasMatch(value)) {
    return 'Username can only contain letters, numbers, underscore, dash, and dot';
  }
  return null;
}

// Amount validation
String? validateAmount(String? value) {
  if (value == null || value.isEmpty) {
    return 'Amount is required';
  }
  final amount = double.tryParse(value);
  if (amount == null) {
    return 'Enter a valid amount';
  }
  if (amount <= 0) {
    return 'Amount must be positive';
  }
  return null;
}

// Symbol validation (e.g., EURUSD, BTCUSDT)
String? validateSymbol(String? value) {
  if (value == null || value.isEmpty) {
    return 'Symbol is required';
  }
  if (value.length < 3 || value.length > 10) {
    return 'Symbol must be 3-10 characters';
  }
  if (!RegExp(r'^[A-Za-z0-9]+$').hasMatch(value)) {
    return 'Symbol can only contain letters and numbers';
  }
  return null;
}
