<?php
/**
 * @license MIT
 *
 * Modified by impress-org on 10-September-2024 using Strauss.
 * @see https://github.com/BrianHenryIE/strauss
 */

namespace Give\Vendors\Faker\Provider\hy_AM;

class Company extends \Give\Vendors\Faker\Provider\Company
{
    protected static $formats = [
        '{{lastName}} {{companySuffix}}',
        '{{lastName}} {{companySuffix}}',
        '{{lastName}} {{companySuffix}}',
        '{{lastName}} {{companySuffix}}',
        '{{lastName}} {{companySuffix}}',
        '{{lastName}} {{companySuffix}}',
        '{{lastName}} {{companySuffix}}',
        '{{lastName}} {{companySuffix}}',
        '{{lastName}} եղբայրներ',
    ];

    protected static $catchPhraseWords = [

    ];

    protected static $bsWords = [

    ];

    protected static $companySuffix = ['ՍՊԸ', 'և որդիներ', 'ՓԲԸ', 'ԲԲԸ'];

    /**
     * @example 'Robust full-range hub'
     */
    public function catchPhrase()
    {
        $result = [];

        foreach (static::$catchPhraseWords as &$word) {
            $result[] = static::randomElement($word);
        }

        return implode(' ', $result);
    }

    /**
     * @example 'integrate extensible convergence'
     */
    public function bs()
    {
        $result = [];

        foreach (static::$bsWords as &$word) {
            $result[] = static::randomElement($word);
        }

        return implode(' ', $result);
    }
}
