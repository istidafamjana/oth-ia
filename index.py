<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>بوت الذكاء الاصطناعي</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #4361ee;
            --secondary-color: #3a0ca3;
            --accent-color: #f72585;
            --dark-color: #1a1a2e;
            --light-color: #f8f9fa;
        }
        
        body {
            font-family: 'Tajawal', sans-serif;
            background: linear-gradient(135deg, var(--dark-color), #16213e);
            color: var(--light-color);
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
            flex: 1;
        }
        
        header {
            padding: 30px 0;
            position: relative;
            z-index: 10;
        }
        
        .logo {
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--light-color);
            text-decoration: none;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 20px;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
        }
        
        .logo i {
            margin-left: 15px;
            color: var(--accent-color);
        }
        
        .main-content {
            text-align: center;
            padding: 80px 0;
            position: relative;
        }
        
        .main-content h1 {
            font-size: 4rem;
            margin-bottom: 30px;
            background: linear-gradient(to right, var(--accent-color), var(--primary-color));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            position: relative;
            display: inline-block;
        }
        
        .main-content h1::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 50%;
            height: 4px;
            background: linear-gradient(to right, var(--accent-color), var(--primary-color));
            border-radius: 2px;
        }
        
        .main-content p {
            font-size: 1.5rem;
            max-width: 800px;
            margin: 0 auto 40px;
            line-height: 1.6;
        }
        
        .status {
            font-size: 2rem;
            padding: 20px 40px;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 50px;
            display: inline-block;
            margin-bottom: 50px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            transform-style: preserve-3d;
            transform: perspective(500px) rotateX(5deg);
            transition: all 0.3s ease;
            animation: pulse 2s infinite;
        }
        
        .status:hover {
            transform: perspective(500px) rotateX(5deg) scale(1.05);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4);
        }
        
        @keyframes pulse {
            0% { box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3); }
            50% { box-shadow: 0 10px 40px rgba(247, 37, 133, 0.4); }
            100% { box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3); }
        }
        
        .social-icons {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-top: 50px;
        }
        
        .social-icon {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.8rem;
            color: white;
            text-decoration: none;
            transition: all 0.3s ease;
            transform-style: preserve-3d;
            transform: perspective(500px) rotateY(15deg);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        }
        
        .social-icon:hover {
            transform: perspective(500px) rotateY(15deg) translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
        }
        
        .facebook {
            background: linear-gradient(45deg, #1877f2, #0d5ab9);
        }
        
        .instagram {
            background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
        }
        
        .floating-bubbles {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            z-index: -1;
        }
        
        .bubble {
            position: absolute;
            bottom: -100px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            animation: rise 15s infinite ease-in;
        }
        
        .bubble:nth-child(1) {
            width: 40px;
            height: 40px;
            left: 10%;
            animation-duration: 8s;
        }
        
        .bubble:nth-child(2) {
            width: 20px;
            height: 20px;
            left: 20%;
            animation-duration: 5s;
            animation-delay: 1s;
        }
        
        .bubble:nth-child(3) {
            width: 50px;
            height: 50px;
            left: 35%;
            animation-duration: 7s;
            animation-delay: 2s;
        }
        
        .bubble:nth-child(4) {
            width: 80px;
            height: 80px;
            left: 50%;
            animation-duration: 11s;
            animation-delay: 0s;
        }
        
        .bubble:nth-child(5) {
            width: 35px;
            height: 35px;
            left: 55%;
            animation-duration: 6s;
            animation-delay: 1s;
        }
        
        .bubble:nth-child(6) {
            width: 65px;
            height: 65px;
            left: 65%;
            animation-duration: 8s;
            animation-delay: 3s;
        }
        
        .bubble:nth-child(7) {
            width: 25px;
            height: 25px;
            left: 75%;
            animation-duration: 7s;
            animation-delay: 2s;
        }
        
        .bubble:nth-child(8) {
            width: 45px;
            height: 45px;
            left: 80%;
            animation-duration: 6s;
            animation-delay: 1s;
        }
        
        @keyframes rise {
            0% {
                bottom: -100px;
                transform: translateX(0) rotate(0deg);
                opacity: 0;
            }
            50% {
                transform: translateX(100px) rotate(180deg);
                opacity: 0.6;
            }
            100% {
                bottom: 1080px;
                transform: translateX(-100px) rotate(360deg);
                opacity: 0;
            }
        }
        
        footer {
            text-align: center;
            padding: 30px 0;
            background: rgba(0, 0, 0, 0.2);
            margin-top: auto;
        }
        
        footer p {
            margin: 0;
            font-size: 1.1rem;
        }
        
        @media (max-width: 768px) {
            .main-content h1 {
                font-size: 2.5rem;
            }
            
            .main-content p {
                font-size: 1.2rem;
                padding: 0 20px;
            }
            
            .status {
                font-size: 1.5rem;
                padding: 15px 30px;
            }
            
            .social-icon {
                width: 50px;
                height: 50px;
                font-size: 1.5rem;
            }
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap" rel="stylesheet">
</head>
<body>
    <div class="floating-bubbles">
        <div class="bubble"></div>
        <div class="bubble"></div>
        <div class="bubble"></div>
        <div class="bubble"></div>
        <div class="bubble"></div>
        <div class="bubble"></div>
        <div class="bubble"></div>
        <div class="bubble"></div>
    </div>
    
    <div class="container">
        <header>
            <a href="#" class="logo">
                <span>بوت الذكاء الاصطناعي</span>
                <i class="fas fa-robot"></i>
            </a>
        </header>
        
        <main class="main-content">
            <h1>جاري تطوير الموقع</h1>
            <p>نحن نعمل حالياً على تطوير موقع متكامل لتجربة أفضل مع بوت الذكاء الاصطناعي الخاص بنا. شكراً لصبركم!</p>
            
            <div class="status">
                قريباً سنكون معكم
            </div>
            
            <div class="social-icons">
                <a href="https://www.facebook.com/profile.php?id=61575007499415" class="social-icon facebook" target="_blank">
                    <i class="fab fa-facebook-f"></i>
                </a>
                <a href="https://instagram.com/mx.fo" class="social-icon instagram" target="_blank">
                    <i class="fab fa-instagram"></i>
                </a>
            </div>
        </main>
    </div>
    
    <footer>
        <p>جميع الحقوق محفوظة &copy; 2024 | فريق البوت الذكي</p>
    </footer>
</body>
</html>
