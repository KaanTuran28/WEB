# WEB — Front-end Mini Projects

![HTML](https://img.shields.io/badge/HTML-CSS-orange)
![JavaScript](https://img.shields.io/badge/javascript-vanilla-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

<p align="center"><b><a href="#english">English</a></b> · <b><a href="#türkçe">Türkçe</a></b></p>

---

## English

A collection of small front-end learning projects — static HTML/CSS/JavaScript pages and a few security-education demos. Each folder is self-contained.

### Projects

| Folder | What it is |
|---|---|
| `Web-site/` | A static website for a shipping/transport company (Nakliye). |
| `10 Kasım/` | A commemorative page for 10 November (Atatürk remembrance). |
| `Password-Generator/` | A password generator: pick a length, generate a random password and optionally save it to a file. |
| `Login/` | A login / sign-up / password UI (static pages). |
| `Numara/` | A small playful themed page. |
| `Cyber--Security-Scanners-Demo/` | **Educational** demo pages that illustrate common web-vulnerability categories (XSS, SQL injection, CSRF, LFI/RFI, directory traversal, and so on). UI demonstrations for learning, not real scanners. |
| `Instagram-login-webhook/` | **Educational** demonstration of how a phishing login page works. See the warning below. |

### Running

These are static pages — open any `index.html` in a browser, or serve a folder with `python -m http.server`.

> **Security-education note:** `Cyber--Security-Scanners-Demo/` and `Instagram-login-webhook/` exist to show how these attacks look and work, as study material. `Instagram-login-webhook/` imitates a login form and forwards whatever is typed to a webhook — this is exactly how real credential-phishing works. Use it only against yourself, in an isolated environment, to understand and defend against the technique. Deploying a fake login page to collect other people's credentials is illegal in most jurisdictions. These demos are not affiliated with Instagram or Meta.

### License

MIT — see [LICENSE](./LICENSE). Subprojects that have their own LICENSE keep it.

---

## Türkçe

Küçük ön yüz (front-end) öğrenme projelerinden oluşan bir koleksiyon — statik HTML/CSS/JavaScript sayfaları ve birkaç güvenlik eğitimi demosu. Her klasör kendi içinde bağımsızdır.

### Projeler

| Klasör | Nedir |
|---|---|
| `Web-site/` | Bir nakliye/taşımacılık firması için statik web sitesi. |
| `10 Kasım/` | 10 Kasım (Atatürk'ü anma) için anma sayfası. |
| `Password-Generator/` | Şifre oluşturucu: uzunluk seçilir, rastgele şifre üretilir ve isteğe bağlı olarak dosyaya kaydedilebilir. |
| `Login/` | Giriş / kayıt / şifre arayüzü (statik sayfalar). |
| `Numara/` | Küçük, eğlenceli temalı bir sayfa. |
| `Cyber--Security-Scanners-Demo/` | Yaygın web zafiyeti kategorilerini (XSS, SQL enjeksiyonu, CSRF, LFI/RFI, dizin gezme vb.) gösteren **eğitim amaçlı** demo sayfaları. Öğrenme için arayüz gösterimleri; gerçek tarayıcılar değil. |
| `Instagram-login-webhook/` | Bir oltalama (phishing) giriş sayfasının nasıl çalıştığını gösteren **eğitim amaçlı** demo. Aşağıdaki uyarıya bakın. |

### Çalıştırma

Bunlar statik sayfalardır — herhangi bir `index.html` dosyasını tarayıcıda açın ya da klasörü `python -m http.server` ile yayınlayın.

> **Güvenlik eğitimi notu:** `Cyber--Security-Scanners-Demo/` ve `Instagram-login-webhook/`, bu saldırıların nasıl göründüğünü ve çalıştığını öğrenmek için hazırlanmış çalışma materyalidir. `Instagram-login-webhook/` bir giriş formunu taklit eder ve girilen bilgileri bir webhook'a iletir — gerçek kimlik bilgisi oltalaması tam olarak böyle çalışır. Bunu yalnızca tekniği anlamak ve ona karşı savunma geliştirmek için, izole bir ortamda kendinize karşı kullanın. Başkalarının kimlik bilgilerini toplamak için sahte bir giriş sayfası yayınlamak çoğu ülkede yasa dışıdır. Bu demolar Instagram veya Meta ile ilişkili değildir.

### Lisans

MIT — bkz. [LICENSE](./LICENSE). Kendi LICENSE dosyası olan alt projeler onu korur.
