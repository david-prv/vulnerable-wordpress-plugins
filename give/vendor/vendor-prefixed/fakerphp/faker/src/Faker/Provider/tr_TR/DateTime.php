<?php
/**
 * @license MIT
 *
 * Modified by impress-org on 10-September-2024 using Strauss.
 * @see https://github.com/BrianHenryIE/strauss
 */

namespace Give\Vendors\Faker\Provider\tr_TR;

class DateTime extends \Give\Vendors\Faker\Provider\DateTime
{
    public static function amPm($max = 'now')
    {
        return static::dateTime($max)->format('a') === 'am' ? 'öö' : 'ös';
    }

    public static function dayOfWeek($max = 'now')
    {
        $map = [
            'Sunday' => 'Pazar',
            'Monday' => 'Pazartesi',
            'Tuesday' => 'Salı',
            'Wednesday' => 'Çarşamba',
            'Thursday' => 'Perşembe',
            'Friday' => 'Cuma',
            'Saturday' => 'Cumartesi',
        ];
        $week = static::dateTime($max)->format('l');

        return $map[$week] ?? $week;
    }

    public static function monthName($max = 'now')
    {
        $map = [
            'January' => 'Ocak',
            'February' => 'Şubat',
            'March' => 'Mart',
            'April' => 'Nisan',
            'May' => 'Mayıs',
            'June' => 'Haziran',
            'July' => 'Temmuz',
            'August' => 'Ağustos',
            'September' => 'Eylül',
            'October' => 'Ekim',
            'November' => 'Kasım',
            'December' => 'Aralık',
        ];
        $month = static::dateTime($max)->format('F');

        return $map[$month] ?? $month;
    }
}
