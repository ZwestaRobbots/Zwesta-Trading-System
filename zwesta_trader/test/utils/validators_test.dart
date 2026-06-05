import 'package:flutter_test/flutter_test.dart';
import 'package:zwesta_trader/utils/validators.dart';

void main() {
  group('Validators', () {
    group('validateUsername', () {
      test('accepts valid username', () {
        expect(validateUsername('john_doe'), isNull);
        expect(validateUsername('user123'), isNull);
        expect(validateUsername('test-user'), isNull);
      });

      test('rejects invalid username', () {
        expect(validateUsername('ab'), isNotNull); // too short
        expect(validateUsername('a' * 21), isNotNull); // too long
        expect(validateUsername(''), isNotNull); // empty
      });
    });

    group('validateEmail', () {
      test('accepts valid email', () {
        expect(validateEmail('user@example.com'), isNull);
        expect(validateEmail('test.user@domain.co.uk'), isNull);
      });

      test('rejects invalid email', () {
        expect(validateEmail('invalid'), isNotNull);
        expect(validateEmail('user@'), isNotNull);
        expect(validateEmail(''), isNotNull);
      });
    });

    group('validatePassword', () {
      test('accepts NIST-compliant password', () {
        expect(validatePassword('Password123!'), isNull);
        expect(validatePassword('MyP@ssw0rd'), isNull);
      });

      test('rejects weak password', () {
        expect(validatePassword('short'), isNotNull); // too short
        expect(validatePassword('password123'), isNotNull); // no uppercase
        expect(validatePassword('PASSWORD123'), isNotNull); // no lowercase
        expect(validatePassword('Password'), isNotNull); // no digit
      });
    });

    group('validateAmount', () {
      test('accepts valid amount', () {
        expect(validateAmount('100.00'), isNull);
        expect(validateAmount('50.50'), isNull);
        expect(validateAmount('1000'), isNull);
      });

      test('rejects invalid amount', () {
        expect(validateAmount('invalid'), isNotNull);
        expect(validateAmount('-100'), isNotNull); // negative
        expect(validateAmount(''), isNotNull);
      });
    });

    group('validateSymbol', () {
      test('accepts valid symbol', () {
        expect(validateSymbol('EURUSD'), isNull);
        expect(validateSymbol('BTCUSDT'), isNull);
        expect(validateSymbol('GBP'), isNull);
      });

      test('rejects invalid symbol', () {
        expect(validateSymbol('EU'), isNotNull); // too short
        expect(validateSymbol('THISISVERYLONG'), isNotNull); // too long
        expect(validateSymbol(''), isNotNull);
      });
    });
  });
}
