<?php
/**
 * @license MIT
 *
 * Modified by impress-org on 10-September-2024 using Strauss.
 * @see https://github.com/BrianHenryIE/strauss
 */

namespace Give\Vendors\Faker\Provider\el_CY;

class Company extends \Give\Vendors\Faker\Provider\Company
{
    protected static $companySuffix = [
        'ΛΤΔ',
        'Δημόσια εταιρεία',
        '& Υιοι',
        '& ΣΙΑ',
    ];

    protected static $formats = [
        '{{lastName}} {{companySuffix}}',
        '{{lastName}}-{{lastName}}',
    ];
}
