<?php
/**
 * @license MIT
 *
 * Modified by impress-org on 10-September-2024 using Strauss.
 * @see https://github.com/BrianHenryIE/strauss
 */

namespace Give\Vendors\Faker\Provider\hu_HU;

class Payment extends \Give\Vendors\Faker\Provider\Payment
{
    /**
     * International Bank Account Number (IBAN)
     *
     * @see http://en.wikipedia.org/wiki/International_Bank_Account_Number
     *
     * @param string $prefix      for generating bank account number of a specific bank
     * @param string $countryCode ISO 3166-1 alpha-2 country code
     * @param int    $length      total length without country code and 2 check digits
     *
     * @return string
     */
    public static function bankAccountNumber($prefix = '', $countryCode = 'HU', $length = null)
    {
        return static::iban($countryCode, $prefix, $length);
    }
}
