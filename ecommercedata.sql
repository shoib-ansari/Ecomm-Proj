-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 24, 2020 at 11:22 AM
-- Server version: 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ecommercedata`
--

--
-- Dumping data for table `offers_offer`
--

INSERT INTO `offers_offer` (`id`, `name`, `image`, `discount`, `end_offer`, `notification`) VALUES
(1, 'Chirstmas Sale', 'offer_pics/chirst_sale.jpg', 30, 1, 'get 30% off on selected products on this christmas'),
(2, 'Flash sale', 'offer_pics/8.jpg', 40, 0, 'get 40% off on selected products on this flash offer'),
(3, 'End of year', 'offer_pics/eoy.jpg', 50, 1, 'get 50% off on selected products on this end of year sale');

--
-- Dumping data for table `offers_promocodes`
--

INSERT INTO `offers_promocodes` (`id`, `image`, `code`, `describtion`, `min_transaction`, `max_cashback`, `cashback_type`, `cashback`, `applicabe_for_transactions`) VALUES
(1, 'offer_image/c1.png', 'supersave', 'Get 50% off  on minimum purchase of 2000. Earn Maximum cashback upto rs.1500', 2000, 1500, '1', 50, 1),
(2, 'offer_image/c2.png', 'shopsale', 'Get upto 75% discount on minimum purchase of rs 100. Max discount is rs.1500', 100, 1500, '1', 75, 1),
(3, 'offer_image/c3.png', 'CouponCountry', 'Flat Rs. 300 back on minimum purchase of Rs.1500.  Available 5 times per user.', 1500, 300, '2', 300, 5);

--
-- Dumping data for table `products_color_variation`
--

INSERT INTO `products_color_variation` (`id`, `color`, `Image_one`, `Image_two`, `Image_three`, `Image_four`, `product_id`) VALUES
(19, 'Transparent', 'Product_Images/s2.jpg', 'Product_Images/s3.jpg', 'Product_Images/s5.jpg', '', 13),
(6, 'white', 'Product_Images/254237-955852.jpg', 'Product_Images/ada.jpg', 'Product_Images/ae.jpg', 'Product_Images/white_shirt.jpg', 3),
(7, 'Blue', 'Product_Images/121.jpg', 'Product_Images/81XpoZZ5YL._UY606_.jpg', 'Product_Images/1212.jpeg', 'Product_Images/2112.jpg', 3),
(8, 'Blue', 'Product_Images/232.jpg', 'Product_Images/2323.jpg', 'Product_Images/8635642_fpx.jpg', 'Product_Images/sdsda.jpg', 4),
(9, 'Cerulean Blue', 'Product_Images/b.jpg', '', '', '', 5),
(10, 'Navy', 'Product_Images/c.jpg', '', '', '', 6),
(11, 'Cream', 'Product_Images/d.jpg', '', '', '', 6),
(12, 'Khakhi', 'Product_Images/e.jpg', '', '', '', 6),
(13, 'LIGHT BLUE', 'Product_Images/f.jpg', '', '', '', 7),
(14, 'Blue', 'Product_Images/g.jpg', 'Product_Images/b1.jpg', 'Product_Images/b2.jpg', 'Product_Images/b3.jpg', 8),
(15, 'Black', 'Product_Images/t2.jpg', 'Product_Images/t3_J6uyByW.jpg', 'Product_Images/t4_WlkI5uY.jpg', '', 9),
(18, 'rinq', 'Product_Images/a.jpg', 'Product_Images/b_6ukwpTV.jpg', '', '', 12),
(17, 'Matte Black', 'Product_Images/c5.jpg', '', '', '', 11),
(20, 'Blue', 'Product_Images/b2_YDd7snx.jpg', 'Product_Images/b3_7tNhadP.jpg', 'Product_Images/b4.jpg', '', 14),
(21, 'Matte Black', 'Product_Images/i4.jpg', 'Product_Images/i1.jpg', 'Product_Images/i2.jpg', '', 15),
(22, 'Matte Pink', 'Product_Images/p4.jpg', 'Product_Images/p2.jpg', 'Product_Images/p1.jpg', '', 16),
(23, 'Electroplate Red', 'Product_Images/o4.jpg', 'Product_Images/o2.jpg', 'Product_Images/o1.jpg', '', 17),
(24, 'Blue', 'Product_Images/f4.jpg', 'Product_Images/f2.jpg', 'Product_Images/f1.jpg', '', 18),
(25, 'Maroon-Black', 'Product_Images/t4_dtParoP.jpg', 'Product_Images/t3_bsTfyGO.jpg', 'Product_Images/t2_KReIbOo.jpg', '', 19),
(26, 'Black-Maroon', 'Product_Images/t4_vYO9RMr.jpg', 'Product_Images/t3_B9LNKQp.jpg', 'Product_Images/t1_RjS41aL.jpg', '', 19),
(27, 'Off-White', 'Product_Images/j5.jpg', 'Product_Images/j4.jpg', 'Product_Images/j3.jpg', 'Product_Images/j2.jpg', 20),
(28, 'Blue-Dark', 'Product_Images/jb1.jpg', 'Product_Images/jb2.jpg', 'Product_Images/jb4.jpg', 'Product_Images/jb3.jpg', 20),
(29, 'Ice Blue', 'Product_Images/ji5.jpg', 'Product_Images/ji4.jpg', 'Product_Images/ji3.jpg', 'Product_Images/ji2.jpg', 20),
(30, 'Light Blue', 'Product_Images/li1.jpg', 'Product_Images/li2.jpg', 'Product_Images/li3.jpg', 'Product_Images/li4.jpg', 20),
(31, 'Azure', 'Product_Images/gj1_pZGoWoa.jpg', 'Product_Images/gj2.jpg', 'Product_Images/gj3.jpg', 'Product_Images/gj4.jpg', 21),
(32, 'White', 'Product_Images/wg3.jpg', 'Product_Images/wg4.jpg', 'Product_Images/wg1.jpg', 'Product_Images/wg2.jpg', 21),
(33, 'Black', 'Product_Images/bj2.jpg', 'Product_Images/bj1.jpg', 'Product_Images/bj3.jpg', 'Product_Images/bj5.jpg', 21),
(34, 'Black', 'Product_Images/kj5.jpg', 'Product_Images/kj4.jpg', 'Product_Images/kj3.jpg', 'Product_Images/kj2.jpg', 22),
(35, 'chikoo', 'Product_Images/ck2.jpg', 'Product_Images/ck1.jpg', '', '', 22);

--
-- Dumping data for table `products_finalcategory`
--

INSERT INTO `products_finalcategory` (`id`, `name`, `main_category_id`, `sub_category_id`) VALUES
(1, 'Shirt', 1, 1),
(2, 'Jeans', 1, 1),
(3, 'Trousers', 1, 1),
(4, 'jeans', 1, 3),
(5, 'top', 1, 3),
(6, 'Shirts', 1, 3),
(7, 'Jeans', 1, 4),
(8, 'Gown', 1, 3),
(9, 't-shirts', 1, 4),
(10, 'Note 8 pro', 2, 5),
(11, 'note 7s', 2, 5),
(12, 'k20', 2, 5),
(13, 'Galaxy note7', 2, 6),
(14, 'M 30', 2, 6),
(15, 'M20', 2, 6),
(16, 'i phone x', 2, 7),
(17, 'i phone 11', 2, 7),
(18, 'i phone XR', 2, 7),
(19, 'Oppo F5', 2, 8),
(20, 'Oppo F11', 2, 8),
(21, 'shoes', 3, 11),
(22, 'sleepers', 3, 11),
(23, 'sandals', 3, 12);

--
-- Dumping data for table `products_maincategory`
--

INSERT INTO `products_maincategory` (`id`, `name`) VALUES
(1, 'Clothes'),
(2, 'Mobile Covers'),
(3, 'Footwear');

--
-- Dumping data for table `products_product`
--

INSERT INTO `products_product` (`id`, `Product_Name`, `Price`, `Current_Price`, `Offer_price`, `Description`, `Size`, `color`, `Total_stock`, `Keywords`, `Return_allowed`, `date`, `image`, `rating`, `total_ratings`, `Final_category_id`, `Main_category_id`, `offer_id`, `sub_category_id`, `brand`) VALUES
(8, 'Jeans for boy', 1999, 809, NULL, 'Our little champ will look his best when wearing this handsome Shirt and Jeans set . This regular-fit set is comfortable to wear and exhibits a fine finish. This set features attractive design and looks just irresistible. Arshia Fashions a noteworthy manufacturer, exporter and supplier of a wide collection of Kids wear. Here you can find a wide range kids ethnic wear and western wear which includes kurta pyjamas, indo western, sherwani, pathani suit set and t-shirt, Jeans, trouser, shorts etc', '', '', NULL, 'Jeans for boy', 1, '2019-12-13', 'Product_Images/b.jpg', '0.0', 0, 7, 1, NULL, 4, 'Gucci'),
(9, 'shirt for boys', 500, 349, NULL, 'Boys cotton t-shirt Black.', '', '', NULL, 'shirt for boys', 1, '2019-12-13', 'Product_Images/c.jpg', '0.0', 0, 9, 1, NULL, 4, 'Siyarams'),
(12, 'dsfgsd', 234, 34, 20, 'sdfds', '', '', NULL, 'fsdf  v', 1, '2019-12-16', 'Product_Images/d.jpg', '0.0', 0, 1, 1, 2, 1, NULL),
(11, 'I phone x cover', 1899, 999, NULL, 'Experience hybrid technology that packs advanced drop protection in a single layer. The Ultra Hybrid combines a shock-absorbing flexible bumper with a rigid back to maximize defensive features. The crystal clear back designed to preserve the original look of the phone. Corners are guarded with Air Cushion Technology that takes all the shock from everyday impacts. Take the Ultra Hybrid to another level by adding personality with personalized items to flaunt with the device.', '', '', NULL, 'I phone x cover', 1, '2019-12-13', 'Product_Images/e.jpg', '0.0', 0, 16, 2, NULL, 7, 'i phone'),
(3, 'Shirts for men', 1000, 800, 0, 'Cotten shirt for men, indian', '', '', NULL, 'shirts for men ,white shirt for men,blue shirt for men', 1, '2019-12-13', 'Product_Images/f.jpg', '3.4', 217, 1, 1, NULL, 1, 'Lee Cooper'),
(4, 'Jeans for men', 800, 650, NULL, 'denim jeans for mrn', '', '', NULL, 'jeans for men, blue,', 1, '2019-12-13', 'Product_Images/g.jpg', '0.0', 0, 2, 1, NULL, 1, NULL),
(5, 'shirt for Man', 1900, 537, NULL, 'Latest Shirt from FINIVO FASHION. This shirt gives a professional look for the true business man. It\'s the perfect day-to-night shirt. Wear it with some slacks to the office and throw on some jeans at night for drinks with the guys. Whatever the occasion this shirt will be your go-to. The style you want and the feel you need all rolled into this shirt.\r\n\r\nImportant information', '', '', NULL, 'shirt For Man ,Cotton shirt for men, indian', 1, '2019-12-13', 'Product_Images/b.jpg', '0.0', 0, 1, 1, NULL, 1, 'd-mart'),
(6, 'Trousers for man', 2699, 599, 0, 'Ben Martin men\'s branded cotton trousers created with passion, dedication, hard work and most of all creativity to carve out a masterpiece.', '', '', NULL, 'Trousers for man', 1, '2019-12-13', 'Product_Images/c.jpg', '0.0', 0, 3, 1, NULL, 1, 'Gucci'),
(7, 'Jeans for Girls', 1999, 599, NULL, 'Made of quality denim cotton fabric with elastane, these give you a comfortable stretchable fit that flatters all shapes and sizes.Contrast stitching with durable button and zip closure that make these fit for all-day everyday wear.Choose from a range of classic denims with modern twists for an updated casual look. It is perfect for semi formal or casual occasion', '', '', NULL, 'Jeans for Girls', 1, '2019-12-13', 'Product_Images/d.jpg', '0.0', 0, 4, 1, NULL, 3, 'd-mart'),
(13, 'Samsung M 30 cover', 399, 99, 0, 'Welcome to the world of Solimo - a place where and great value go hand in hand. Every Solimo product is carefully built to deliver exceptional quality. Right from the materials used, to detailed quality checks, to thoughtful improvements, quality is at the core of everything we do. We invest our resources only on what is important to you and minimize costs on things like packaging, advertising and other extras that don’t add value. This helps us keep our costs low and create products that deliver more value for the price you pay. Expect a little more every time you buy a Solimo product.', '', '', NULL, 'Samsung M 30 cover , mobile cover, cover,samsung', 1, '2019-12-17', 'Product_Images/a_w7e8TX8.jpg', '0.0', 0, 14, 2, NULL, 6, 'samsung'),
(14, 'Samsung M 20 cover', 999, 149, 0, 'Tarkan brings to you a new horizon for protecting and presenting your favourite gadgets. Uniquely crafted by the best designers in the industry. Its Vogue design, and superior quality stands itself a class apart. We value your gadgets and splash tonnes of creativity in creating every accessory. Because, we realise that a case is much more than providing mere protection. It\'s an expression. Expression of love for your gadget. Expression of your personality. Expression of your thoughts. And the expression of your passion.', '', '', NULL, 'Samsung M 20 cover , samsung , cover , samsung', 1, '2019-12-17', 'Product_Images/b_vaNLrrS.jpg', '0.0', 0, 15, 2, NULL, 6, 'samsung'),
(15, 'I Phone 11 cover', 1899, 899, NULL, 'Hybrid technology that is made of a TPU bumper with a durable PC back .', '', '', NULL, 'I Phone 11 cover', 1, '2019-12-17', 'Product_Images/i3.jpg', '0.0', 0, 17, 2, NULL, 7, 'apple'),
(16, 'I Phone XR Cover', 999, 299, 0, 'A Perfect match to your phone, makes your phone personalized and absorbing. With this luxury and gorgeous cover your phone will be more eye-catching.\r\n\r\nUnique design allows easy access to all buttons, controls and ports without having to remove the case.\r\n\r\nPerfect cutouts and slim design allow you to maximize the functionality of your phone.\r\n\r\nFunctional design, exquisite workmanship, durable material, double enjoyment for appearance and practicality.', '', '', NULL, 'I Phone XR Cover', 1, '2019-12-17', 'Product_Images/p3.jpg', '0.0', 0, 18, 2, NULL, 7, 'apple'),
(17, 'Oppo F5 Cover', 1400, 299, 0, 'A Perfect match to your phone, makes your phone personalized and absorbing. With this luxury and gorgeous cover your iphone will be more eye-catching.\r\n\r\nUnique design allows easy access to all buttons, controls and ports without having to remove the case.\r\n\r\nPerfect cutouts and slim design allow you to maximize the functionality of your phone.\r\n\r\nFunctional design, exquisite workmanship, durable material, double enjoyment for appearance and practicality.', '', '', NULL, 'Oppo F5 Cover', 1, '2019-12-17', 'Product_Images/o3.jpg', '0.0', 0, 19, 2, NULL, 8, 'oppo'),
(18, 'Oppo F11 Cover', 999, 295, 0, 'Made from environmental and non-toxic TPU material. Simple and special design. Light reflection on the phone’s back makes it even more beautiful. Weave texture. Lightweight and thin. Scratch and impact resistant. Anti-fingerprint and oil contamination. Tiny holes for heat dissipation. Camera protection. Helps you take great looking pictures. [Soft TPU]: Made of soft TPU material with stylish design, this case is lightweight and thin, add no bulk. [Heat Dissipation] Built with many breathable and heat dissipation holes, it can help to lower the temperature of your Phone when you are watching video or gaming. [Wireless Charge Friendly]: It supports wireless charge with no need to take off the case. [Impact Resistant]: All the corners have air cushion design for shock and impact resistant, provide better protection for your expensive Device. [Accurate Cutouts]: Accurate cutouts for easy access to all buttons and features, raised lip for camera protection.', '', '', NULL, 'Oppo F11 Cover', 1, '2019-12-17', 'Product_Images/f3.jpg', '0.0', 0, 20, 2, NULL, 8, 'oppo'),
(19, 'Shirt  For Men', 899, 379, 265, 'Fall in love with the soft texture as you adorn this full sleeves shirt from house of GRITSTONES. Your skin will love the feel of this dress wear as it is fashioned using the material that is famous for comfort. Style it with denim jeans for a casual look with an edge.', '', '', NULL, 'Shirt  For Men', 1, '2019-12-20', 'Product_Images/t1.jpg', '0.0', 0, 1, 1, 1, 1, 'Raymond'),
(20, 'Jeans for Men', 1599, 579, 0, 'Skinny fit jeans\r\n99% Cotton 1% Spandex\r\nZip fly with button closure\r\nMid rise jeans\r\nThe model (height 6\'1 and waist 32") is wearing a size 31', '', '', NULL, 'Jeans for Men', 1, '2019-12-20', 'Product_Images/j1.jpg', '0.0', 0, 2, 1, NULL, 1, 'D&G'),
(21, 'Jeans For Girls', 1999, 499, 0, 'This slim fit denim jeans is for women. Pair this piece with heels or flats for a stunning look.', '', '', NULL, 'Jeans For Girls', 1, '2019-12-20', 'Product_Images/gj1.jpg', '0.0', 0, 4, 1, NULL, 3, 'Lee Cooper'),
(22, 'Jeans For Boys', 1400, 673, 0, 'AdBucks presents to you wide range of boys cargos. About Us: Established in 1992, we are a prominent manufacturer and trader of Boys,Girls, Gents, Ladies Jeans / Jeggings / Leggings / Shorts, Readymade Dress, Shirts, T-Shirts, Ladies Tops under the Brand Name of "AdBucks". Our organization works on the principles of unmatched quality, speedy delivery and maximum customer satisfaction. Our quality centric approach has enabled us to meet the demands of our reputed clients successfully and win their undeterred trust; thus becoming a renowned name in the industry ourselves.', '', 'red', NULL, 'Jeans For Boys', 1, '2019-12-20', 'Product_Images/kj1.jpg', '0.0', 0, 7, 1, NULL, 4, 'Gucci');

--
-- Dumping data for table `products_reviews`
--

INSERT INTO `products_reviews` (`id`, `review`, `rating`, `product_id`, `user_id`) VALUES
(26, 'Hii', 4, 3, 5),
(25, 'HUHIHGUBJGH', 4, 3, 7);

--
-- Dumping data for table `products_size_variation`
--

INSERT INTO `products_size_variation` (`id`, `size`, `Quantity`, `color_id`) VALUES
(1, 'XL', '10', 6),
(2, 'L', '20', 6),
(3, 'S', '40', 6),
(4, 'M', '15', 7),
(5, 'XS', '20', 7),
(6, 'XL', '20', 7),
(7, '38', '10', 9),
(8, '28', '10', 10),
(9, '30', '5', 10),
(10, '32', '8', 10),
(11, '34', '12', 10),
(12, '36', '15', 10),
(13, '38', '20', 10),
(14, '34', '5', 13),
(15, '36', '15', 13),
(16, '2-3 years', '20', 14),
(17, '3-4 years', '15', 14),
(18, '4-5 years', '2', 14),
(19, '5-6 years', '8', 14),
(20, '3-4 years', '50', 15),
(21, '7-8 year', '20', 15),
(22, 'Small', '10', 25),
(23, 'Mediuam', '20', 25),
(24, 'Large', '5', 25),
(25, 'x-Large', '4', 25),
(26, '28', '40', 27),
(27, '30', '8', 27),
(28, '32', '15', 27),
(29, '34', '30', 27),
(30, '36', '20', 27),
(31, '28', '28', 31),
(32, '30', '20', 31),
(33, '32', '5', 31),
(34, '34', '15', 31),
(35, '36', '30', 31),
(36, '40', '10', 31),
(37, '18-24 Month', '10', 34),
(38, '2 - 3 years', '15', 34),
(39, '3 - 4 years', '20', 34),
(40, '4 - 5 years', '30', 34),
(41, '5 - 6 years', '25', 34),
(42, '6 - 7 years', '60', 34),
(43, '7 - 8 years', '99', 34);

--
-- Dumping data for table `products_subcategory`
--

INSERT INTO `products_subcategory` (`id`, `name`, `main_category_id`) VALUES
(1, 'Men', 1),
(2, 'Women', 1),
(3, 'Girls', 1),
(4, 'Boys', 1),
(5, 'Xiaomi', 2),
(6, 'Samsung', 2),
(7, 'Apple', 2),
(8, 'Oppo', 2),
(9, 'Vivo', 2),
(10, 'Nokia', 2),
(11, 'men', 3),
(12, 'women', 3);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
