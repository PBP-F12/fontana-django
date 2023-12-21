from auths.forms import AuthorRegistrationForm
from main.models import Book

author_form = AuthorRegistrationForm(
    {"full_name": "Harper Lee", "username": "harperlee", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("harperlee")
print("To Kill a Mockingbird")
book = Book(author_id=author_instance, book_title="To Kill a Mockingbird", description='The unforgettable novel of a childhood in a sleepy Southern town and the crisis of conscience that rocked it. "To Kill A Mockingbird" became both an instant bestseller and a critical success when it was first published in 1960. It went on to win the Pulitzer Prize in 1961 and was later made into an Academy Award-winning film, also a classic.Compassionate, dramatic, and deeply moving, "To Kill A Mockingbird" takes readers to the roots of human behavior - to innocence and experience, kindness and cruelty, love and hatred, humor and pathos. Now with over 18 million copies in print and translated into forty languages, this regional story by a young Alabama woman claims universal appeal. Harper Lee always considered her book to be a simple love story. Today it is regarded as a masterpiece of American literature.', avg_rating=4.27, num_rating=5691311, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1553383690i/2657.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "J.K. Rowling", "username": "j.k.rowling", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("j.k.rowling")
print("Harry Potter and the Philosopher’s Stone (Harry Potter, #1)")
book = Book(author_id=author_instance, book_title="Harry Potter and the Philosopher’s Stone (Harry Potter, #1)", description='Harry Potter thinks he is an ordinary boy - until he is rescued by an owl, taken to Hogwarts School of Witchcraft and Wizardry, learns to play Quidditch and does battle in a deadly duel. The Reason ... HARRY POTTER IS A WIZARD!',
            avg_rating=4.47, num_rating=9278135, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1170803558l/72193.jpg")
book.save()
print("Harry Potter and the Deathly Hallows (Harry Potter, #7)")
book = Book(author_id=author_instance, book_title="Harry Potter and the Deathly Hallows (Harry Potter, #7)", description='Harry has been burdened with a dark, dangerous and seemingly impossible task: that of locating and destroying Voldemort\u0027s remaining Horcruxes. Never has Harry felt so alone, or faced a future so full of shadows. But Harry must somehow find within himself the strength to complete the task he has been given. He must leave the warmth, safety and companionship of The Burrow and follow without fear or hesitation the inexorable path laid out for him...In this final, seventh installment of the Harry Potter series, J.K. Rowling unveils in spectacular fashion the answers to the many questions that have been so eagerly awaited.',
            avg_rating=4.62, num_rating=3468276, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1663805647i/136251.jpg")
book.save()
print("Harry Potter and the Prisoner of Azkaban (Harry Potter, #3)")
book = Book(author_id=author_instance, book_title="Harry Potter and the Prisoner of Azkaban (Harry Potter, #3)", description='Harry Potter, along with his best friends, Ron and Hermione, is about to start his third year at Hogwarts School of Witchcraft and Wizardry. Harry can\u0027t wait to get back to school after the summer holidays. (Who wouldn\u0027t if they lived with the horrible Dursleys?) But when Harry gets to Hogwarts, the atmosphere is tense. There\u0027s an escaped mass murderer on the loose, and the sinister prison guards of Azkaban have been called in to guard the school...',
            avg_rating=4.58, num_rating=3808160, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1630547330i/5.jpg")
book.save()
print("Harry Potter and the Goblet of Fire (Harry Potter, #4)")
book = Book(author_id=author_instance, book_title="Harry Potter and the Goblet of Fire (Harry Potter, #4)", description='It is the summer holidays and soon Harry Potter will be starting his fourth year at Hogwarts School of Witchcraft and Wizardry. Harry is counting the days: there are new spells to be learnt, more Quidditch to be played, and Hogwarts castle to continue exploring. But Harry needs to be careful - there are unexpected dangers lurking...',
            avg_rating=4.56, num_rating=3397378, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1554006152i/6.jpg")
book.save()
print("Harry Potter and the Half-Blood Prince (Harry Potter, #6)")
book = Book(author_id=author_instance, book_title="Harry Potter and the Half-Blood Prince (Harry Potter, #6)", description='It is the middle of the summer, but there is an unseasonal mist pressing against the windowpanes. Harry Potter is waiting nervously in his bedroom at the Dursleys\u0027 house in Privet Drive for a visit from Professor Dumbledore himself. One of the last times he saw the Headmaster was in a fierce one-to-one duel with Lord Voldemort, and Harry can\u0027t quite believe that Professor Dumbledore will actually appear at the Dursleys\u0027 of all places. Why is the Professor coming to visit him now? What is it that cannot wait until Harry returns to Hogwarts in a few weeks\u0027 time? Harry\u0027s sixth year at Hogwarts has already got off to an unusual start, as the worlds of Muggle and magic start to intertwine...', avg_rating=4.58, num_rating=3048651, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1587697303i/1.jpg")
book.save()
print("Harry Potter and the Chamber of Secrets (Harry Potter, #2)")
book = Book(author_id=author_instance, book_title="Harry Potter and the Chamber of Secrets (Harry Potter, #2)", description='Ever since Harry Potter had come home for the summer, the Dursleys had been so mean and hideous that all Harry wanted was to get back to the Hogwarts School for Witchcraft and Wizardry. But just as he’s packing his bags, Harry receives a warning from a strange impish creature who says that if Harry returns to Hogwarts, disaster will strike.And strike it does. For in Harry’s second year at Hogwarts, fresh torments and horrors arise, including an outrageously stuck-up new professor and a spirit who haunts the girls’ bathroom. But then the real trouble begins – someone is turning Hogwarts students to stone. Could it be Draco Malfoy, a more poisonous rival than ever? Could it possibly be Hagrid, whose mysterious past is finally told? Or could it be the one everyone at Hogwarts most suspects… Harry Potter himself!', avg_rating=4.43, num_rating=3597747, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1474169725i/15881.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Jane Austen", "username": "janeausten", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("janeausten")
print("Pride and Prejudice")
book = Book(author_id=author_instance, book_title="Pride and Prejudice", description='Since its immediate success in 1813, Pride and Prejudice has remained one of the most popular novels in the English language. Jane Austen called this brilliant work "her own darling child" and its vivacious heroine, Elizabeth Bennet, "as delightful a creature as ever appeared in print." The romantic clash between the opinionated Elizabeth and her proud beau, Mr. Darcy, is a splendid performance of civilized sparring. And Jane Austen\u0027s radiant wit sparkles as her characters dance a delicate quadrille of flirtation and intrigue, making this book the most superb comedy of manners of Regency England.Alternate cover edition of ISBN 9780679783268',
            avg_rating=4.28, num_rating=3944155, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1320399351i/1885.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Anne Frank", "username": "annefrank", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("annefrank")
print("The Diary of a Young Girl")
book = Book(author_id=author_instance, book_title="The Diary of a Young Girl", description='Discovered in the attic in which she spent the last years of her life, Anne Frank’s remarkable diary has become a world classic—a powerful reminder of the horrors of war and an eloquent testament to the human spirit. In 1942, with the Nazis occupying Holland, a thirteen-year-old Jewish girl and her family fled their home in Amsterdam and went into hiding. For the next two years, until their whereabouts were betrayed to the Gestapo, the Franks and another family lived cloistered in the “Secret Annexe” of an old office building. Cut off from the outside world, they faced hunger, boredom, the constant cruelties of living in confined quarters, and the ever-present threat of discovery and death. In her diary Anne Frank recorded vivid impressions of her experiences during this period. By turns thoughtful, moving, and surprisingly humorous, her account offers a fascinating commentary on human courage and frailty and a compelling self-portrait of a sensitive and spirited young woman whose promise was tragically cut short.--back cover', avg_rating=4.18, num_rating=3488438, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1560816565i/48855.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "George Orwell", "username": "georgeorwell", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("georgeorwell")
print("Animal Farm")
book = Book(author_id=author_instance, book_title="Animal Farm", description='Librarian\u0027s note: There is an Alternate Cover Edition for this edition of this book here.A farm is taken over by its overworked, mistreated animals. With flaming idealism and stirring slogans, they set out to create a paradise of progress, justice, and equality. Thus the stage is set for one of the most telling satiric fables ever penned –a razor-edged fairy tale for grown-ups that records the evolution from revolution against tyranny to a totalitarianism just as terrible. When Animal Farm was first published, Stalinist Russia was seen as its target. Today it is devastatingly clear that wherever and whenever freedom is attacked, under whatever banner, the cutting clarity and savage comedy of George Orwell’s masterpiece have a meaning and message still ferociously fresh.', avg_rating=3.98, num_rating=3575172, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1325861570i/170448.jpg")
book.save()
print("1984")
book = Book(author_id=author_instance, book_title="1984", description='The new novel by George Orwell is the major work towards which all his previous writing has pointed. Critics have hailed it as his "most solid, most brilliant" work. Though the story of Nineteen Eighty-Four takes place thirty-five years hence, it is in every sense timely. The scene is London, where there has been no new housing since 1950 and where the city-wide slums are called Victory Mansions. Science has abandoned Man for the State. As every citizen knows only too well, war is peace.To Winston Smith, a young man who works in the Ministry of Truth (Minitru for short), come two people who transform this life completely. One is Julia, whom he meets after she hands him a slip reading, "I love you." The other is O\u0027Brien, who tells him, "We shall meet in the place where there is no darkness." The way in which Winston is betrayed by the one and, against his own desires and instincts, ultimately betrays the other, makes a story of mounting drama and suspense.Alternate cover edition can be found here.', avg_rating=4.19, num_rating=4201429, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1657781256i/61439040.jpg")
book.save()

author_form = AuthorRegistrationForm({"full_name": "Antoine de Saint-Exupéry",
                                     "username": "antoinedesaint_exupery", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("antoinedesaint_exupery")
print("The Little Prince")
book = Book(author_id=author_instance, book_title="The Little Prince", description='A pilot stranded in the desert awakes one morning to see, standing before him, the most extraordinary little fellow. "Please," asks the stranger, "draw me a sheep." And the pilot realizes that when life\u0027s events are too difficult to understand, there is no choice but to succumb to their mysteries. He pulls out pencil and paper... And thus begins this wise and enchanting fable that, in teaching the secret of what is really important in life, has changed forever the world for its readers.Few stories are as widely read and as universally cherished by children and adults alike as The Little Prince, presented here in a stunning new translation with carefully restored artwork. The definitive edition of a worldwide classic, it will capture the hearts of readers of all ages.', avg_rating=4.32, num_rating=1924063, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1367545443i/157993.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "F. Scott Fitzgerald", "username": "f.scottfitzgerald", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("f.scottfitzgerald")
print("The Great Gatsby")
book = Book(author_id=author_instance, book_title="The Great Gatsby", description='Alternate Cover Edition ISBN: 0743273567 (ISBN13: 9780743273565)The Great Gatsby, F. Scott Fitzgerald\u0027s third book, stands as the supreme achievement of his career. This exemplary novel of the Jazz Age has been acclaimed by generations of readers. The story of the fabulously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan, of lavish parties on Long Island at a time when The New York Times noted "gin was the national drink and sex the national obsession," it is an exquisitely crafted tale of America in the 1920s.The Great Gatsby is one of the great classics of twentieth-century literature.(from the back cover)',
            avg_rating=3.93, num_rating=4839642, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1490528560i/4671.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "J.D. Salinger", "username": "j.d.salinger", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("j.d.salinger")
print("The Catcher in the Rye")
book = Book(author_id=author_instance, book_title="The Catcher in the Rye", description='It\u0027s Christmas time and Holden Caulfield has just been expelled from yet another school...Fleeing the crooks at Pencey Prep, he pinballs around New York City seeking solace in fleeting encounters—shooting the bull with strangers in dive hotels, wandering alone round Central Park, getting beaten up by pimps and cut down by erstwhile girlfriends. The city is beautiful and terrible, in all its neon loneliness and seedy glamour, its mingled sense of possibility and emptiness. Holden passes through it like a ghost, thinking always of his kid sister Phoebe, the only person who really understands him, and his determination to escape the phonies and find a life of true meaning.The Catcher in the Rye is an all-time classic in coming-of-age literature- an elegy to teenage alienation, capturing the deeply human need for connection and the bewildering sense of loss as we leave childhood behind. J.D. Salinger\u0027s (1919–2010) classic novel of teenage angst and rebellion was first published in 1951. The novel was included on Time\u0027s 2005 list of the 100 best English-language novels written since 1923. It was named by Modern Library and its readers as one of the 100 best English-language novels of the 20th century. It has been frequently challenged in the court for its liberal use of profanity and portrayal of sexuality and in the 1950\u0027s and 60\u0027s it was the novel that every teenage boy wants to read.', avg_rating=3.81, num_rating=3315881, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1398034300i/5107.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "J.R.R. Tolkien", "username": "j.r.r.tolkien", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("j.r.r.tolkien")
print("The Lord of the Rings")
book = Book(author_id=author_instance, book_title="The Lord of the Rings", description='One Ring to rule them all, One Ring to find them, One Ring to bring them all and in the darkness bind themIn ancient times the Rings of Power were crafted by the Elven-smiths, and Sauron, the Dark Lord, forged the One Ring, filling it with his own power so that he could rule all others. But the One Ring was taken from him, and though he sought it throughout Middle-earth, it remained lost to him. After many ages it fell by chance into the hands of the hobbit Bilbo Baggins.From Sauron\u0027s fastness in the Dark Tower of Mordor, his power spread far and wide. Sauron gathered all the Great Rings to him, but always he searched for the One Ring that would complete his dominion.When Bilbo reached his eleventy-first birthday he disappeared, bequeathing to his young cousin Frodo the Ruling Ring and a perilous quest: to journey across Middle-earth, deep into the shadow of the Dark Lord, and destroy the Ring by casting it into the Cracks of Doom.The Lord of the Rings tells of the great quest undertaken by Frodo and the Fellowship of the Ring: Gandalf the Wizard; the hobbits Merry, Pippin, and Sam; Gimli the Dwarf; Legolas the Elf; Boromir of Gondor; and a tall, mysterious stranger called Strider.', avg_rating=4.52, num_rating=644766, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1566425108i/33.jpg")
book.save()
print("The Hobbit (The Lord of the Rings, #0)")
book = Book(author_id=author_instance, book_title="The Hobbit (The Lord of the Rings, #0)", description='In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort.Written for J.R.R. Tolkien’s own children, The Hobbit met with instant critical acclaim when it was first published in 1937. Now recognized as a timeless classic, this introduction to the hobbit Bilbo Baggins, the wizard Gandalf, Gollum, and the spectacular world of Middle-earth recounts of the adventures of a reluctant hero, a powerful and dangerous ring, and the cruel dragon Smaug the Magnificent. The text in this 372-page paperback edition is based on that first published in Great Britain by Collins Modern Classics (1998), and includes a note on the text by Douglas A. Anderson (2001).', avg_rating=4.28, num_rating=3662325, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1546071216i/5907.jpg")
book.save()
print("Tolkien On Fairy-stories")
book = Book(author_id=author_instance, book_title="Tolkien On Fairy-stories", description='J.R.R. Tolkien\u0027s On Fairy-stories is his most-studied and most-quoted essay, an exemplary personal statement of his own views on the role of imagination in literature, and an intellectual tour de force vital for understanding Tolkien\u0027s achievement in writing  The Lord of the Rings. Contained within is an introduction to Tolkien\u0027s original 1939 lecture and the history of the writing of On Fairy-stories, with previously unseen material. Here, at last, Flieger and Anderson reveal the extraordinary genesis of this seminal work and discuss how the conclusions that Tolkien reached during the composition of the essay would shape his writing for the rest of his life.',
            avg_rating=4.32, num_rating=3744, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1326706200i/1362112.jpg")
book.save()
print("The Fellowship of the Ring (The Lord of the Rings, #1)")
book = Book(author_id=author_instance, book_title="The Fellowship of the Ring (The Lord of the Rings, #1)", description='One Ring to rule them all, One Ring to find them, One Ring to bring them all and in the darkness bind them.In ancient times the Rings of Power were crafted by the Elven-smiths, and Sauron, the Dark Lord, forged the One Ring, filling it with his own power so that he could rule all others. But the One Ring was taken from him, and though he sought it throughout Middle-earth, it remained lost to him. After many ages it fell into the hands of Bilbo Baggins, as told in The Hobbit.In a sleepy village in the Shire, young Frodo Baggins finds himself faced with an immense task, as his elderly cousin Bilbo entrusts the Ring to his care. Frodo must leave his home and make a perilous journey across Middle-earth to the Cracks of Doom, there to destroy the Ring and foil the Dark Lord in his evil purpose.', avg_rating=4.38, num_rating=2686920, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1654215925i/61215351.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Markus Zusak", "username": "markuszusak", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("markuszusak")
print("The Book Thief")
book = Book(author_id=author_instance, book_title="The Book Thief", description='Librarian\u0027s note: An alternate cover edition can be found hereIt is 1939. Nazi Germany. The country is holding its breath. Death has never been busier, and will be busier still.By her brother\u0027s graveside, Liesel\u0027s life is changed when she picks up a single object, partially hidden in the snow. It is The Gravedigger\u0027s Handbook, left behind there by accident, and it is her first act of book thievery. So begins a love affair with books and words, as Liesel, with the help of her accordian-playing foster father, learns to read. Soon she is stealing books from Nazi book-burnings, the mayor\u0027s wife\u0027s library, wherever there are books to be found.But these are dangerous times. When Liesel\u0027s foster family hides a Jew in their basement, Liesel\u0027s world is both opened up, and closed down.In superbly crafted writing that burns with intensity, award-winning author Markus Zusak has given us one of the most enduring stories of our time.(Note: this title was not published as YA fiction)', avg_rating=4.39, num_rating=2364659, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1522157426i/19063.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Charlotte Brontë", "username": "charlottebronte", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("charlottebronte")
print("Jane Eyre")
book = Book(author_id=author_instance, book_title="Jane Eyre", description='Orphaned as a child, Jane has felt an outcast her whole young life. Her courage is tested once again when she arrives at Thornfield Hall, where she has been hired by the brooding, proud Edward Rochester to care for his ward Adèle. Jane finds herself drawn to his troubled yet kind spirit. She falls in love. Hard. But there is a terrifying secret inside the gloomy, forbidding Thornfield Hall. Is Rochester hiding from Jane? Will Jane be left heartbroken and exiled once again?',
            avg_rating=4.14, num_rating=1975582, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1557343311i/10210.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "C.S. Lewis", "username": "c.s.lewis", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("c.s.lewis")
print("The Chronicles of Narnia (Chronicles of Narnia, #1-7)")
book = Book(author_id=author_instance, book_title="The Chronicles of Narnia (Chronicles of Narnia, #1-7)", description='Librarian note: An alternate cover for this edition can be found here: 2005.Journeys to the end of the world, fantastic creatures, and epic battles between good and evil—what more could any reader ask for in one book? The book that has it all is The Lion, the Witch and the Wardrobe, written in 1949 by Clive Staples Lewis. But Lewis did not stop there. Six more books followed, and together they became known as The Chronicles of Narnia.For the past fifty years, The Chronicles of Narnia have transcended the fantasy genre to become part of the canon of classic literature. Each of the seven books is a masterpiece, drawing the reader into a land where magic meets reality, and the result is a fictional world whose scope has fascinated generations.This edition presents all seven books—unabridged—in one impressive volume. The books are presented here in chronlogical order, each chapter graced with an illustration by the original artist, Pauline Baynes. Deceptively simple and direct, The Chronicles of Narnia continue to captivate fans with adventures, characters, and truths that speak to readers of all ages, even fifty years after they were first published.', avg_rating=4.27, num_rating=617006, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1661032875i/11127.jpg")
book.save()
print("The Lion, the Witch and the Wardrobe (Chronicles of Narnia, #1)")
book = Book(author_id=author_instance, book_title="The Lion, the Witch and the Wardrobe (Chronicles of Narnia, #1)", description='Narnia… the land beyond the wardrobe door, a secret place frozen in eternal winter, a magical country waiting to be set free.Lucy is the first to find the secret of the wardrobe in the professor\u0027s mysterious old house. At first her brothers and sister don\u0027t believe her when she tells of her visit to the land of Narnia. But soon Edmund, then Peter and Susan step through the wardrobe themselves. In Narnia they find a country buried under the evil enchantment of the White Witch. When they meet the Lion Aslan, they realize they\u0027ve been called to a great adventure and bravely join the battle to free Narnia from the Witch\u0027s sinister spell.',
            avg_rating=4.23, num_rating=2620424, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1353029077i/100915.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "William Golding", "username": "williamgolding", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("williamgolding")
print("Lord of the Flies")
book = Book(author_id=author_instance, book_title="Lord of the Flies", description='At the dawn of the next world war, a plane crashes on an uncharted island, stranding a group of schoolboys. At first, with no adult supervision, their freedom is something to celebrate; this far from civilization the boys can do anything they want. Anything. They attempt to forge their own society, failing, however, in the face of terror, sin and evil. And as order collapses, as strange howls echo in the night, as terror begins its reign, the hope of adventure seems as far from reality as the hope of being rescued. Labeled a parable, an allegory, a myth, a morality tale, a parody, a political treatise, even a vision of the apocalypse, Lord of the Flies is perhaps our most memorable novel about “the end of innocence, the darkness of man’s heart.”', avg_rating=3.69, num_rating=2738919, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1327869409i/7624.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "William Shakespeare", "username": "williamshakespeare", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("williamshakespeare")
print("Romeo and Juliet")
book = Book(author_id=author_instance, book_title="Romeo and Juliet", description='In Romeo and Juliet, Shakespeare creates a violent world, in which two young people fall in love. It is not simply that their families disapprove; the Montagues and the Capulets are engaged in a blood feud.In this death-filled setting, the movement from love at first sight to the lovers’ final union in death seems almost inevitable. And yet, this play set in an extraordinary world has become the quintessential story of young love. In part because of its exquisite language, it is easy to respond as if it were about all young lovers.',
            avg_rating=3.74, num_rating=2469086, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1629680008i/18135.jpg")
book.save()
print("Hamlet")
book = Book(author_id=author_instance, book_title="Hamlet", description='Among Shakespeare\u0027s plays, "Hamlet" is considered by many his masterpiece. Among actors, the role of Hamlet, Prince of Denmark, is considered the jewel in the crown of a triumphant theatrical career. Now Kenneth Branagh plays the leading role and co-directs a brillant ensemble performance. Three generations of legendary leading actors, many of whom first assembled for the Oscar-winning film "Henry V", gather here to perform the rarely heard complete version of the play. This clear, subtly nuanced, stunning dramatization, presented by The Renaissance Theatre Company in association with "Bbc" Broadcasting, features such luminaries as Sir John Gielgud, Derek Jacobi, Emma Thompson and Christopher Ravenscroft. It combines a full cast with stirring music and sound effects to bring this magnificent Shakespearen classic vividly to life. Revealing new riches with each listening, this production of "Hamlet" is an invaluable aid for students, teachers and all true lovers of Shakespeare - a recording to be treasured for decades to come.', avg_rating=4.02, num_rating=890747, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1351051208i/1420.jpg")
book.save()
print("Macbeth")
book = Book(author_id=author_instance, book_title="Macbeth", description='One night on the heath, the brave and respected general Macbeth encounters three witches who foretell that he will become king of Scotland. At first sceptical, he’s urged on by the ruthless, single-minded ambitions of Lady Macbeth, who suffers none of her husband’s doubt. But seeing the prophecy through to the bloody end leads them both spiralling into paranoia, tyranny, madness, and murder.This shocking tragedy - a violent caution to those seeking power for its own sake - is, to this day, one of Shakespeare’s most popular and influential masterpieces.',
            avg_rating=3.9, num_rating=839821, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1459795224i/8852.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Khaled Hosseini", "username": "khaledhosseini", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("khaledhosseini")
print("The Kite Runner")
book = Book(author_id=author_instance, book_title="The Kite Runner", description='1970s Afghanistan: Twelve-year-old Amir is desperate to win the local kite-fighting tournament and his loyal friend Hassan promises to help him. But neither of the boys can foresee what would happen to Hassan that afternoon, an event that is to shatter their lives. After the Russians invade and the family is forced to flee to America, Amir realises that one day he must return to an Afghanistan under Taliban rule to find the one thing that his new world cannot grant him: redemption.',
            avg_rating=4.33, num_rating=2954721, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1579036753i/77203.jpg")
book.save()
print("A Thousand Splendid Suns")
book = Book(author_id=author_instance, book_title="A Thousand Splendid Suns", description='Mariam is only fifteen when she is sent to Kabul to marry the troubled and bitter Rasheed, who is thirty years her senior. Nearly two decades later, in a climate of growing unrest, tragedy strikes fifteen-year-old Laila, who must leave her home and join Mariam\u0027s unhappy household. Laila and Mariam are to find consolation in each other, their friendship to grow as deep as the bond between sisters, as strong as the ties between mother and daughter. With the passing of time comes Taliban rule over Afghanistan, the streets of Kabul loud with the sound of gunfire and bombs, life a desperate struggle against starvation, brutality and fear, the women\u0027s endurance tested beyond their worst imaginings. Yet love can move people to act in unexpected ways, lead them to overcome the most daunting obstacles with a startling heroism. In the end it is love that triumphs over death and destruction."A Thousand Splendid Suns" is a portrait of a wounded country and a story of family and friendship, of an unforgiving time, an unlikely bond, and an indestructible love.', avg_rating=4.42, num_rating=1428213, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1655336738i/128029.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Lois Lowry", "username": "loislowry", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("loislowry")
print("The Giver (The Giver, #1)")
book = Book(author_id=author_instance, book_title="The Giver (The Giver, #1)", description='At the age of twelve, Jonas, a young boy from a seemingly utopian, futuristic world, is singled out to receive special training from The Giver, who alone holds the memories of the true joys and pain of life.',
            avg_rating=4.12, num_rating=2285401, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1342493368i/3636.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Shel Silverstein", "username": "shelsilverstein", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("shelsilverstein")
print("The Giving Tree")
book = Book(author_id=author_instance, book_title="The Giving Tree", description='Once there was a tree...and she loved a little boy."So begins a story of unforgettable perception, beautifully written and illustrated by the gifted and versatile Shel Silverstein.Every day the boy would come to the tree to eat her apples, swing from her branches, or slide down her trunk...and the tree was happy. But as the boy grew older he began to want more from the tree, and the tree gave and gave and gave.This is a tender story, touched with sadness, aglow with consolation. Shel Silverstein has created a moving parable for readers of all ages that offers an affecting interpretation of the gift of giving and a serene acceptance of another\u0027s capacity to love in return.',
            avg_rating=4.38, num_rating=1067524, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1174210942i/370493.jpg")
book.save()
print("Where the Sidewalk Ends")
book = Book(author_id=author_instance, book_title="Where the Sidewalk Ends", description='Come in... for where the sidewalk ends, Shel Silverstein\u0027s world begins.Shel Silverstein, the New York Times bestselling author of The Giving Tree, A Light in the Attic, Falling Up, and Every Thing On It, has created a poetry collection that is outrageously funny and deeply profound. You\u0027ll meet a boy who turns into a TV set, and a girl who eats a whale. The Unicorn and the Bloath live there, and so does Sarah Cynthia Sylvia Stout who will not take the garbage out. It is a place where you wash your shadow and plant diamond gardens, a place where shoes fly, sisters are auctioned off, and crocodiles go to the dentist.Shel Silverstein\u0027s masterful collection of poems and drawings stretches the bounds of imagination and will be cherished by readers of all ages.', avg_rating=4.32, num_rating=1336522, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1168052448i/30119.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "E.B. White", "username": "e.b.white", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("e.b.white")
print("Charlotte's Web")
book = Book(author_id=author_instance, book_title="Charlotte's Web", description='This beloved book by E. B. White, author of Stuart Little and The Trumpet of the Swan, is a classic of children\u0027s literature that is "just about perfect." This high-quality paperback features vibrant illustrations colorized by Rosemary Wells!Some Pig. Humble. Radiant. These are the words in Charlotte\u0027s Web, high up in Zuckerman\u0027s barn. Charlotte\u0027s spiderweb tells of her feelings for a little pig named Wilbur, who simply wants a friend. They also express the love of a girl named Fern, who saved Wilbur\u0027s life when he was born the runt of his litter.E. B. White\u0027s Newbery Honor Book is a tender novel of friendship, love, life, and death that will continue to be enjoyed by generations to come. This edition contains newly color illustrations by Garth Williams, the acclaimed illustrator of E. B. White\u0027s Stuart Little and Laura Ingalls Wilder\u0027s Little House series, among many other books.', avg_rating=4.19, num_rating=1724889, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1628267712i/24178.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Louisa May Alcott", "username": "louisamayalcott", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("louisamayalcott")
print("Little Women")
book = Book(author_id=author_instance, book_title="Little Women", description='This is an alternate cover edition of ISBN 9780451529305.Generations of readers young and old, male and female, have fallen in love with the March sisters of Louisa May Alcott’s most popular and enduring novel, Little Women. Here are talented tomboy and author-to-be Jo, tragically frail Beth, beautiful Meg, and romantic, spoiled Amy, united in their devotion to each other and their struggles to survive in New England during the Civil War.It is no secret that Alcott based Little Women on her own early life. While her father, the freethinking reformer and abolitionist Bronson Alcott, hobnobbed with such eminent male authors as Emerson, Thoreau, and Hawthorne, Louisa supported herself and her sisters with "woman’s work,” including sewing, doing laundry, and acting as a domestic servant. But she soon discovered she could make more money writing. Little Women brought her lasting fame and fortune, and far from being the "girl’s book” her publisher requested, it explores such timeless themes as love and death, war and peace, the conflict between personal ambition and family responsibilities, and the clash of cultures between Europe and America.', avg_rating=4.14, num_rating=2085559, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1562690475i/1934.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Suzanne Collins", "username": "suzannecollins", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("suzannecollins")
print("The Hunger Games (The Hunger Games, #1)")
book = Book(author_id=author_instance, book_title="The Hunger Games (The Hunger Games, #1)", description='Could you survive on your own in the wild, with every one out to make sure you don\u0027t live to see the morning?In the ruins of a place once known as North America lies the nation of Panem, a shining Capitol surrounded by twelve outlying districts. The Capitol is harsh and cruel and keeps the districts in line by forcing them all to send one boy and one girl between the ages of twelve and eighteen to participate in the annual Hunger Games, a fight to the death on live TV.Sixteen-year-old Katniss Everdeen, who lives alone with her mother and younger sister, regards it as a death sentence when she steps forward to take her sister\u0027s place in the Games. But Katniss has been close to dead before—and survival, for her, is second nature. Without really meaning to, she becomes a contender. But if she is to win, she will have to start making choices that weight survival against humanity and life against love.', avg_rating=4.33, num_rating=7963002, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1586722975i/2767052.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "John Steinbeck", "username": "johnsteinbeck", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("johnsteinbeck")
print("Of Mice and Men")
book = Book(author_id=author_instance, book_title="Of Mice and Men", description='“I got you to look after me, and you got me to look after you, and that\u0027swhy.” They are an unlikely pair: George is "small and quick and dark of face"; Lennie, a man of tremendous size, has the mind of a young child. Yet they have formed a "family," clinging together in the face of loneliness and alienation. Laborers in California\u0027s dusty vegetable fields, they hustle work when they can, living a hand-to-mouth existence. But George and Lennie have a plan: to own an acre of land and a shack they can call their own.While the powerlessness of the laboring class is a recurring theme in Steinbeck\u0027s work of the late 1930s, he narrowed his focus when composing \u0027Of Mice and Men\u0027 (1937), creating an intimate portrait of two men facing a world marked by petty tyranny, misunderstanding, jealousy, and callousness. But though the scope is narrow, the theme is universal: a friendship and a shared dream that makes an individual\u0027s existence meaningful.A unique perspective on life\u0027s hardships, this story has achieved the status of timeless classic due to its remarkable success as a novel, a Broadway play, and three acclaimed films.', avg_rating=3.88, num_rating=2396235, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1511302904i/890.jpg")
book.save()
print("The Grapes of Wrath")
book = Book(author_id=author_instance, book_title="The Grapes of Wrath", description='The Pulitzer Prize-winning epic of the Great Depression, a book that galvanized—and sometimes outraged—millions of readers.First published in 1939, Steinbeck’s Pulitzer Prize-winning epic of the Great Depression chronicles the Dust Bowl migration of the 1930s and tells the story of one Oklahoma farm family, the Joads—driven from their homestead and forced to travel west to the promised land of California. Out of their trials and their repeated collisions against the hard realities of an America divided into Haves and Have-Nots evolves a drama that is intensely human yet majestic in its scale and moral vision, elemental yet plainspoken, tragic but ultimately stirring in its human dignity. A portrait of the conflict between the powerful and the powerless, of one man’s fierce reaction to injustice, and of one woman’s stoical strength, the novel captures the horrors of the Great Depression and probes into the very nature of equality and justice in America. At once a naturalistic epic, captivity narrative, road novel, and transcendental gospel, Steinbeck’s powerful landmark novel is perhaps the most American of American Classics.', avg_rating=4, num_rating=864334, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1375670575i/18114322.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Ray Bradbury", "username": "raybradbury", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("raybradbury")
print("Fahrenheit 451")
book = Book(author_id=author_instance, book_title="Fahrenheit 451", description='Sixty years after its original publication, Ray Bradbury’s internationally acclaimed novel Fahrenheit 451 stands as a classic of world literature set in a bleak, dystopian future. Today its message has grown more relevant than ever before.Guy Montag is a fireman. His job is to destroy the most illegal of commodities, the printed book, along with the houses in which they are hidden. Montag never questions the destruction and ruin his actions produce, returning each day to his bland life and wife, Mildred, who spends all day with her television “family.” But when he meets an eccentric young neighbor, Clarisse, who introduces him to a past where people didn’t live in fear and to a present where one sees the world through the ideas in books instead of the mindless chatter of television, Montag begins to question everything he has ever known.', avg_rating=3.97, num_rating=2215889, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1383718290i/13079982.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Dr. Seuss", "username": "dr.seuss", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("dr.seuss")
print("Green Eggs and Ham")
book = Book(author_id=author_instance, book_title="Green Eggs and Ham", description='“Do you like green eggs and ham?” asks Sam-I-am in this Beginner Book by Dr. Seuss. In a house or with a mouse? In a boat or with a goat? On a train or in a tree? Sam keeps asking persistently. With unmistakable characters and signature rhymes, Dr. Seuss’s beloved favorite has cemented its place as a children’s classic. In this most famous of cumulative tales, the list of places to enjoy green eggs and ham, and friends to enjoy them with, gets longer and longer. Follow Sam-I-am as he insists that this unusual treat is indeed a delectable snack to be savored everywhere and in every way. Originally created by Dr. Seuss, Beginner Books encourage children to read all by themselves, with simple words and illustrations that give clues to their meaning.', avg_rating=4.3, num_rating=735514, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1673212751i/23772.jpg")
book.save()
print("The Cat in the Hat (The Cat in the Hat, #1)")
book = Book(author_id=author_instance, book_title="The Cat in the Hat (The Cat in the Hat, #1)", description='Have a ball with Dr. Seuss and the Cat in the Hat in this classic picture book...but don\u0027t forget to clean up your mess! Then he said That is that.And then he was goneWith a tip of his hat.A dreary day turns into a wild romp when this beloved story introduces readers to the Cat in the Hat and his troublemaking friends, Thing 1 and Thing 2 – And don\u0027t forget Fish! A favorite among kids, parents and teachers, this story uses simple words and basic rhyme to encourage and delight beginning readers.Originally created by Dr. Seuss himself, Beginner Books are fun, funny, and easy to read. These unjacketed hardcover early readers encourage children to read all on their own, using simple words and illustrations. Smaller than the classic large format Seuss picture books like The Lorax and Oh, The Places You\u0027ll Go!, these portable packages are perfect for practicing readers ages 3-7, and lucky parents too!', avg_rating=4.18, num_rating=515170, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1468890477i/233093.jpg")
book.save()
print("Oh, the Places You'll Go!")
book = Book(author_id=author_instance, book_title="Oh, the Places You'll Go!", description='For out-starting upstarts of all ages, here is a wonderfully wise and blessedly brief graduation speech from the one and only Dr. Seuss!In his inimitable, humorous verse and pictures, he addresses the Great Balancing Act (life itself, and the ups and downs it presents) while encouraging us to find the success that lies within us."And will you succeed?Yes! You will indeed!(98 and ¾ percent guaranteed.)"A modern classic, Oh, the Places You\u0027ll Go! was first published one year before Dr. Seuss\u0027s death at the age of eighty-seven. In a mere fifty-six pages, Dr, Seuss managed to impart a lifetime of wisdom. It is the perfect send-off for children starting out in the maze of life, be they nursery school grads or newly-minted PhD\u0027s. Everyone will find it inspired good fun.With his unique combination of hilarious stories, zany pictures and riotous rhymes, Dr. Seuss has been delighting young children and helping them learn to read for over fifty years. Creator of the wonderfully anarchic \u0027Cat in the Hat\u0027, and ranked among the world\u0027s top children\u0027s authors, Dr. Seuss is a global best-seller, with nearly half a billion books sold worldwide.', avg_rating=4.36, num_rating=387581, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1630510695i/191139.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Emily Brontë", "username": "emilybronte", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("emilybronte")
print("Wuthering Heights")
book = Book(author_id=author_instance, book_title="Wuthering Heights", description='You can find the redesigned cover of this edition HERE.At the centre of this novel is the passionate love between Catherine Earnshaw and Heathcliff - recounted with such emotional intensity that a plain tale of the Yorkshire moors acquires the depth and simplicity of ancient tragedy.This best-selling Norton Critical Edition is based on the 1847 first edition of the novel. For the Fourth Edition, the editor has collated the 1847 text with several modern editions and has corrected a number of variants, including accidentals. The text is accompanied by entirely new explanatory annotations.New to the fourth Edition are twelve of Emily Bronte\u0027s letters regarding the publication of the 1847 edition of Wuthering Heights as well as the evolution of the 1850 edition, prose and poetry selections by the author, four reviews of the novel, and poetry selections by the author, four reviews of the novel, and Edward Chitham\u0027s insightful and informative chronology of the creative process behind the beloved work.Five major critical interpretations of Wuthering Heights are included, three of them new to the Fourth Edition. A Stuart Daley considers the importance of chronology in the novel. J. Hillis Miller examines Wuthering Heights\u0027s problems of genre and critical reputation. Sandra M. Gilbert assesses the role of Victorian Christianity plays in the novel, while Martha Nussbaum traces the novel\u0027s romanticism. Finally, Lin Haire-Sargeant scrutinizes the role of Heathcliff in film adaptations of Wuthering Heights. A Chronology and updated Selected Bibliography are also included.', avg_rating=3.88, num_rating=1684275, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1388212715i/6185.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Lewis Carroll", "username": "lewiscarroll", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("lewiscarroll")
print("Alice's Adventures in Wonderland / Through the Looking-Glass")
book = Book(author_id=author_instance, book_title="Alice's Adventures in Wonderland / Through the Looking-Glass", description='I can\u0027t explain myself, I\u0027m afraid, sir," said Alice, "Because I\u0027m not myself, you see."When Alice sees a white rabbit take a watch out of its waistcoat pocket she decides to follow it, and a sequence of most unusual events is set in motion. This mini book contains the entire topsy-turvy stories of Alice\u0027s Adventures in Wonderland and Through the Looking-Glass, accompanied by practical notes and Martina Pelouso\u0027s memorable full-colour illustrations.',
            avg_rating=4.06, num_rating=536708, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1630487234i/24213.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Oscar Wilde", "username": "oscarwilde", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("oscarwilde")
print("The Picture of Dorian Gray")
book = Book(author_id=author_instance, book_title="The Picture of Dorian Gray", description='Oscar Wilde’s only novel is the dreamlike story of a young man who sells his soul for eternal youth and beauty.In this celebrated work Wilde forged a devastating portrait of the effects of evil and debauchery on a young aesthete in late-19th-century England. Combining elements of the Gothic horror novel and decadent French fiction, the book centers on a striking premise: As Dorian Gray sinks into a life of crime and gross sensuality, his body retains perfect youth and vigor while his recently painted portrait grows day by day into a hideous record of evil, which he must keep hidden from the world. For over a century, this mesmerizing tale of horror and suspense has enjoyed wide popularity. It ranks as one of Wilde\u0027s most important creations and among the classic achievements of its kind.', avg_rating=4.12, num_rating=1370605, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1546103428i/5297.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Elie Wiesel", "username": "eliewiesel", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("eliewiesel")
print("Night  (The Night Trilogy, #1)")
book = Book(author_id=author_instance, book_title="Night  (The Night Trilogy, #1)", description='Born in the town of Sighet, Transylvania, Elie Wiesel was a teenager when he and his family were taken from their home in 1944 to Auschwitz concentration camp, and then to Buchenwald. Night is the terrifying record of Elie Wiesel\u0027s memories of the death of his family, the death of his own innocence, and his despair as a deeply observant Jew confronting the absolute evil of man. This new translation by his wife and most frequent translator, Marion Wiesel, corrects important details and presents the most accurate rendering in English of Elie Wiesel\u0027s testimony to what happened in the camps and of his unforgettable message that this horror must simply never be allowed to happen again.',
            avg_rating=4.36, num_rating=1170381, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1575073611i/1617.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Margaret Mitchell", "username": "margaretmitchell", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("margaretmitchell")
print("Gone with the Wind")
book = Book(author_id=author_instance, book_title="Gone with the Wind", description='Scarlett O\u0027Hara, the beautiful, spoiled daughter of a well-to-do Georgia plantation owner, must use every means at her disposal to claw her way out of the poverty she finds herself in after Sherman\u0027s March to the Sea.',
            avg_rating=4.3, num_rating=1179002, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1551144577i/18405.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Anonymous", "username": "anonymous", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("anonymous")
print("The Holy Bible: King James Version")
book = Book(author_id=author_instance, book_title="The Holy Bible: King James Version", description='An Award or Presentation Bible in the King James Version: ideal as a gift or to keep The full text of the Popular size King James or Authorized Version Bible, in a straightforward black imitation leather hardback binding.',
            avg_rating=4.43, num_rating=272793, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1631816305i/1923820.jpg")
book.save()
print("القرآن الكريم")
book = Book(author_id=author_instance, book_title="القرآن الكريم", description='The Quran (English pronunciation: /kɔrˈɑːn/; Arabic: القرآن‎ al-qurʾān, IPA: [qurˈʔaːn], literally meaning "the recitation"), also transliterated Qur\u0027an, Koran, Al-Coran, Coran, Kur\u0027an, and Al-Qur\u0027an, is the central religious text of Islam, which Muslims believe to be the verbatim word of God (Arabic: الله‎, Allah). The Quran is composed of verses (Ayat) that make up 114 chapters (suras) of unequal length which are classified either as Meccan (المكية) or Medinan (المدنية) depending upon the place and time of their claimed revelation. Muslims believe the Quran to be verbally revealed through the angel Jibrīl (Gabriel) from God to Muhammad gradually over a period of approximately 23 years beginning on 22 December 609 CE, when Muhammad was 40, and concluding in 632 CE, the year of his death.Muslims regard the Quran as the main miracle of Muhammad, the proof of his prophethood and the culmination of a series of divine messages that started with the messages revealed to Adam, regarded in Islam as the first prophet, and continued with Suhuf Ibrahim (Scrolls of Abraham), the Tawrat (Torah or Pentateuch) of Moses, the Zabur (Tehillim or Book of Psalms) of David, and the Injil (Gospel) of Jesus. The Quran assumes familiarity with major narratives recounted in Jewish and Christian scriptures, summarizing some, dwelling at length on others and in some cases presenting alternative accounts and interpretations of events. The Quran describes itself as a book of guidance, sometimes offering detailed accounts of specific historical events, and often emphasizing the moral significance of an event over its narrative sequence.', avg_rating=4.38, num_rating=65695, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1275263838i/646462.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Douglas Adams", "username": "douglasadams", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("douglasadams")
print("The Hitchhiker's Guide to the Galaxy (The Hitchhiker's Guide to the Galaxy, #1)")
book = Book(author_id=author_instance, book_title="The Hitchhiker's Guide to the Galaxy (The Hitchhiker's Guide to the Galaxy, #1)", description='Seconds before the Earth is demolished to make way for a galactic freeway, Arthur Dent is plucked off the planet by his friend Ford Prefect, a researcher for the revised edition of The Hitchhiker\u0027s Guide to the Galaxy who, for the last fifteen years, has been posing as an out-of-work actor.Together this dynamic pair begin a journey through space aided by quotes from The Hitchhiker\u0027s Guide ("A towel is about the most massively useful thing an interstellar hitchhiker can have") and a galaxy-full of fellow travelers: Zaphod Beeblebrox--the two-headed, three-armed ex-hippie and totally out-to-lunch president of the galaxy; Trillian, Zaphod\u0027s girlfriend (formally Tricia McMillan), whom Arthur tried to pick up at a cocktail party once upon a time zone; Marvin, a paranoid, brilliant, and chronically depressed robot; Veet Voojagig, a former graduate student who is obsessed with the disappearance of all the ballpoint pens he bought over the years.Where are these pens? Why are we born? Why do we die? Why do we spend so much time between wearing digital watches? For all the answers stick your thumb to the stars. And don\u0027t forget to bring a towel!', avg_rating=4.23, num_rating=1739532, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1559986152l/386162.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Mark Twain", "username": "marktwain", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("marktwain")
print("The Adventures of Huckleberry Finn")
book = Book(author_id=author_instance, book_title="The Adventures of Huckleberry Finn", description='A nineteenth-century boy from a Mississippi River town recounts his adventures as he travels down the river with a runaway slave, encountering a family involved in a feud, two scoundrels pretending to be royalty, and Tom Sawyer\u0027s aunt who mistakes him for Tom.',
            avg_rating=3.83, num_rating=1237071, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1546096879i/2956.jpg")
book.save()
print("The Adventures of Tom Sawyer")
book = Book(author_id=author_instance, book_title="The Adventures of Tom Sawyer", description='The Adventures of Tom Sawyer revolves around the youthful adventures of the novel\u0027s schoolboy protagonist, Thomas Sawyer, whose reputation precedes him for causing mischief and strife. Tom lives with his Aunt Polly, half-brother Sid, and cousin Mary in the quaint town of St. Petersburg, just off the shore of the Mississippi River. St. Petersburg is described as a typical small-town atmosphere where the Christian faith is predominant, the social network is close-knit, and familiarity resides.  Unlike his brother Sid, Tom receives "lickings" from his Aunt Polly; ever the mischief-maker, would rather play hooky than attend school and often sneaks out his bedroom window at night to adventure with his friend, Huckleberry Finn ­ the town\u0027s social outcast. Tom, despite his dread of schooling, is extremely clever and would normally get away with his pranks if Sid were not such a "tattle-tale."  As punishment for skipping school to go swimming, Aunt Polly assigns Tom the chore of whitewashing the fence surrounding the house. In a brilliant scheme, Tom is able to con the neighborhood boys into completing the chore for him, managing to convince them of the joys of whitewashing. At school, Tom is equally as flamboyant, and attracts attention by chasing other boys, yelling, and running around. With his usual antics, Tom attempts to catch the eye of Becky Thatcher, a new girl in town, and persuades her to get "engaged" by kissing him. But their romance collapses when she learns Tom has been "engaged" previously to Amy Lawrence. Shortly after Becky shuns him, he accompanies Huckleberry Finn to the graveyard at night, where they witness the murder of Dr. Robinson.Excerpt:"TOM!" No answer. "TOM!" No answer. "What\u0027s gone with that boy,  I wonder? You TOM!" No answer. The old lady pulled her spectacles down and looked over them about the room; then she put them up and looked out under them. She seldom or never looked through them for so small a thing as a boy; they were her state pair, the pride of her heart, and were built for "style," not service—she could have seen through a pair of stove-lids just as well. She looked perplexed for a moment, and then said, not fiercely, but still loud enough for the furniture to hear: "Well, I lay if I get hold of you I\u0027ll—" She did not finish, for by this time she was bending down and punching under the bed with the broom, and so she needed breath to punctuate the punches with. She resurrected nothing but the cat. "I never did see the beat of that boy!', avg_rating=3.92, num_rating=892115, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1404811979i/24583.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Victor Hugo", "username": "victorhugo", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("victorhugo")
print("Les Misérables")
book = Book(author_id=author_instance, book_title="Les Misérables", description='Victor Hugo\u0027s tale of injustice, heroism and love follows the fortunes of Jean Valjean, an escaped convict determined to put his criminal past behind him. But his attempts to become a respected member of the community are constantly put under threat: by his own conscience, when, owing to a case of mistaken identity, another man is arrested in his place; and by the relentless investigations of the dogged Inspector Javert. It is not simply for himself that Valjean must stay free, however, for he has sworn to protect the baby daughter of Fantine, driven to prostitution by poverty.',
            avg_rating=4.2, num_rating=769757, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1411852091i/24280.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Paulo Coelho", "username": "paulocoelho", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("paulocoelho")
print("The Alchemist")
book = Book(author_id=author_instance, book_title="The Alchemist", description='Combining magic, mysticism, wisdom, and wonder into an inspiring tale of self-discovery, The Alchemist has become a modern classic, selling millions of copies around the world and transforming the lives of countless readers across generations.Paulo Coelho\u0027s masterpiece tells the mystical story of Santiago, an Andalusian shepherd boy who yearns to travel in search of a worldly treasure. His quest will lead him to riches far different—and far more satisfying—than he ever imagined. Santiago\u0027s journey teaches us about the essential wisdom of listening to our hearts, recognizing opportunity and learning to read the omens strewn along life\u0027s path, and, most importantly, following our dreams.',
            avg_rating=3.9, num_rating=2792673, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1654371463i/18144590.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Aldous Huxley", "username": "aldoushuxley", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("aldoushuxley")
print("Brave New World / Brave New World Revisited")
book = Book(author_id=author_instance, book_title="Brave New World / Brave New World Revisited", description='The astonishing novel Brave New World, originally published in 1932, presents Aldous Huxley\u0027s vision of the future--of a world utterly transformed. Through the most efficient scientific and psychological engineering, people are genetically designed to be passive and therefore consistently useful to the ruling class. This powerful work of speculative fiction sheds a blazing critical light on the present and is considered to be Aldous Huxley\u0027s most enduring masterpiece.The non-fiction work Brave New World Revisited, published in 1958, is a fascinating work in which Huxley uses his tremendous knowledge of human relations to compare the modern-day world with his prophetic fantasy envisioned in Brave New World, including the threats to humanity, such as over-population, propaganda, and chemical persuasion.', avg_rating=4.16, num_rating=159408, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1331315450i/5479.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Fyodor Dostoevsky", "username": "fyodordostoevsky", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("fyodordostoevsky")
print("Crime and Punishment")
book = Book(author_id=author_instance, book_title="Crime and Punishment", description='Raskolnikov, a destitute and desperate former student, wanders through the slums of St Petersburg and commits a random murder without remorse or regret. He imagines himself to be a great man, a Napoleon: acting for a higher purpose beyond conventional moral law. But as he embarks on a dangerous game of cat and mouse with a suspicious police investigator, Raskolnikov is pursued by the growing voice of his conscience and finds the noose of his own guilt tightening around his neck. Only Sonya, a downtrodden sex worker, can offer the chance of redemption.',
            avg_rating=4.26, num_rating=820645, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1382846449i/7144.jpg")
book.save()
print("The Brothers Karamazov")
book = Book(author_id=author_instance, book_title="The Brothers Karamazov", description='The Brothers Karamazov is a murder mystery, a courtroom drama, and an exploration of erotic rivalry in a series of triangular love affairs involving the “wicked and sentimental” Fyodor Pavlovich Karamazov and his three sons―the impulsive and sensual Dmitri; the coldly rational Ivan; and the healthy, red-cheeked young novice Alyosha. Through the gripping events of their story, Dostoevsky portrays the whole of Russian life, is social and spiritual striving, in what was both the golden age and a tragic turning point in Russian culture.This award-winning translation by Richard Pevear and Larissa Volokhonsky remains true to the verbalinventiveness of Dostoevsky’s prose, preserving the multiple voices, the humor, and the surprising modernity of the original. It is an achievement worthy of Dostoevsky’s last and greatest novel.', avg_rating=4.36, num_rating=304800, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1427728126i/4934.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Kathryn Stockett", "username": "kathrynstockett", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("kathrynstockett")
print("The Help")
book = Book(author_id=author_instance, book_title="The Help", description='Three ordinary women are about to take one extraordinary step.Twenty-two-year-old Skeeter has just returned home after graduating from Ole Miss. She may have a degree, but it is 1962, Mississippi, and her mother will not be happy till Skeeter has a ring on her finger. Skeeter would normally find solace with her beloved maid Constantine, the woman who raised her, but Constantine has disappeared and no one will tell Skeeter where she has gone.Aibileen is a black maid, a wise, regal woman raising her seventeenth white child. Something has shifted inside her after the loss of her own son, who died while his bosses looked the other way. She is devoted to the little girl she looks after, though she knows both their hearts may be broken.Minny, Aibileen\u0027s best friend, is short, fat, and perhaps the sassiest woman in Mississippi. She can cook like nobody\u0027s business, but she can\u0027t mind her tongue, so she\u0027s lost yet another job. Minny finally finds a position working for someone too new to town to know her reputation. But her new boss has secrets of her own.Seemingly as different from one another as can be, these women will nonetheless come together for a clandestine project that will put them all at risk. And why? Because they are suffocating within the lines that define their town and their times. And sometimes lines are made to be crossed.In pitch-perfect voices, Kathryn Stockett creates three extraordinary women whose determination to start a movement of their own forever changes a town, and the way women, mothers, daughters, caregivers, friends, view one another. A deeply moving novel filled with poignancy, humor, and hope, The Help is a timeless and universal story about the lines we abide by, and the ones we don\u0027t. Librarian\u0027s note: An alternate cover edition can be found here', avg_rating=4.47, num_rating=2600987, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1622355533i/4667024.jpg")
book.save()

author_form = AuthorRegistrationForm({"full_name": "Frances Hodgson Burnett",
                                     "username": "franceshodgsonburnett", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("franceshodgsonburnett")
print("The Secret Garden")
book = Book(author_id=author_instance, book_title="The Secret Garden", description='When orphaned Mary Lennox comes to live at her uncle\u0027s great house on the Yorkshire Moors, she finds it full of secrets. The mansion has nearly one hundred rooms, and her uncle keeps himself locked up. And at night, she hears the sound of crying down one of the long corridors. The gardens surrounding the large property are Mary\u0027s only escape. Then, Mary discovers a secret garden, surrounded by walls and locked with a missing key. One day, with the help of two unexpected companions, she discovers a way in. Is everything in the garden dead, or can Mary bring it back to life?One of the most delightful and enduring classics of children\u0027s literature, The Secret Garden has remained a firm favorite with children the world over ever since it made its first appearance. Initially published as a serial story in 1910 in The American Magazine, it was brought out in novel form in 1911.', avg_rating=4.15, num_rating=1097941, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1327873635i/2998.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Arthur Golden", "username": "arthurgolden", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("arthurgolden")
print("Memoirs of a Geisha")
book = Book(author_id=author_instance, book_title="Memoirs of a Geisha", description='A literary sensation and runaway bestseller, this brilliant novel presents with seamless authenticity and exquisite lyricism the true confessions of one of Japan\u0027s most celebrated geisha.In "Memoirs of a Geisha," we enter a world where appearances are paramount; where a girl\u0027s virginity is auctioned to the highest bidder; where women are trained to beguile the most powerful men; and where love is scorned as illusion. It is a unique and triumphant work of fiction - at once romantic, erotic, suspenseful - and completely unforgettable.',
            avg_rating=4.14, num_rating=1929777, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1409595968i/929.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Homer", "username": "homer", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("homer")
print("The Odyssey")
book = Book(author_id=author_instance, book_title="The Odyssey", description='Sing to me of the man, Muse, the man of twists and turnsdriven time and again off course, once he had plunderedthe hallowed heights of Troy.So begins Robert Fagles\u0027 magnificent translation of the Odyssey.If the Iliad is the world\u0027s greatest war epic, then the Odyssey is literature\u0027s grandest evocation of everyman\u0027s journey though life. Odysseus\u0027 reliance on his wit and wiliness for survival in his encounters with divine and natural forces, during his ten-year voyage home to Ithaca after the Trojan War, is at once a timeless human story and an individual test of moral endurance. In the myths and legends that are retold here, Fagles has captured the energy and poetry of Homer\u0027s original in a bold, contemporary idiom, and given us an Odyssey to read aloud, to savor, and to treasure for its sheer lyrical mastery.Renowned classicist Bernard Knox\u0027s superb Introduction and textual commentary provide new insights and background information for the general reader and scholar alike, intensifying the strength of Fagles\u0027 translation.This is an Odyssey to delight both the classicist and the public at large, and to captivate a new generation of Homer\u0027s students.--Robert Fagles, winner of the PEN/Ralph Manheim Medal for Translation and a 1996 Academy Award in Literature from the American Academy of Arts and Letters, presents us with Homer\u0027s best-loved and most accessible poem in a stunning new modern-verse translation.', avg_rating=3.8, num_rating=1017517, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1390173285i/1381.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Charles Dickens", "username": "charlesdickens", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("charlesdickens")
print("A Christmas Carol")
book = Book(author_id=author_instance, book_title="A Christmas Carol", description='\u0027If I had my way, every idiot who goes around with Merry Christmas on his lips, would be boiled with his own pudding, and buried with a stake of holly through his heart. Merry Christmas? Bah humbug!\u0027Introduction and Afterword by Joe WheelerTo bitter, miserly Ebenezer Scrooge, Christmas is just another day. But all that changes when the ghost of his long-dead business partner appears, warning Scrooge to change his ways before it\u0027s too late. Part of the Focus on the Family Great Stories collection, this abridged edition features an in-depth introduction and discussion questions by Joe Wheeler to provide greater understanding for today\u0027s reader. "A Christmas Carol" captures the heart of the holidays like no other novel.', avg_rating=4.07, num_rating=779092, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1406512317i/5326.jpg")
book.save()
print("A Tale of Two Cities")
book = Book(author_id=author_instance, book_title="A Tale of Two Cities", description='A Tale of Two Cities is Charles Dickens’s great historical novel, set against the violent upheaval of the French Revolution. The most famous and perhaps the most popular of his works, it compresses an event of immense complexity to the scale of a family history, with a cast of characters that includes a bloodthirsty ogress and an antihero as believably flawed as any in modern fiction. Though the least typical of the author’s novels, A Tale of Two Cities still underscores many of his enduring themes—imprisonment, injustice, social anarchy, resurrection, and the renunciation that fosters renewal.',
            avg_rating=3.86, num_rating=911758, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1344922523i/1953.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "S.E. Hinton", "username": "s.e.hinton", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("s.e.hinton")
print("The Outsiders")
book = Book(author_id=author_instance, book_title="The Outsiders", description='The Outsiders is about two weeks in the life of a 14-year-old boy. The novel tells the story of Ponyboy Curtis and his struggles with right and wrong in a society in which he believes that he is an outsider. According to Ponyboy, there are two kinds of people in the world: greasers and socs. A soc (short for "social") has money, can get away with just about anything, and has an attitude longer than a limousine. A greaser, on the other hand, always lives on the outside and needs to watch his back. Ponyboy is a greaser, and he\u0027s always been proud of it, even willing to rumble against a gang of socs for the sake of his fellow greasers--until one terrible night when his friend Johnny kills a soc. The murder gets under Ponyboy\u0027s skin, causing his bifurcated world to crumble and teaching him that pain feels the same whether a soc or a greaser.Librarian note: This record is for one of the three editions published with different covers and with ISBN 0-140-38572-X / 978-0-14-038572-4. The records are for the 1988 cover (this record), the 1995 cover, and the 2008 cover which is also the current in-print cover.', avg_rating=4.12, num_rating=1220608, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1442129426i/231804.jpg")
book.save()

author_form = AuthorRegistrationForm({"full_name": "Gabriel García Márquez",
                                     "username": "gabrielgarciamarquez", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("gabrielgarciamarquez")
print("One Hundred Years of Solitude")
book = Book(author_id=author_instance, book_title="One Hundred Years of Solitude", description='The brilliant, bestselling, landmark novel that tells the story of the Buendia family, and chronicles the irreconcilable conflict between the desire for solitude and the need for love—in rich, imaginative prose that has come to define an entire genre known as "magical realism.',
            avg_rating=4.11, num_rating=911512, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1327881361i/320.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "L.M. Montgomery", "username": "l.m.montgomery", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("l.m.montgomery")
print("Anne of Green Gables (Anne of Green Gables, #1)")
book = Book(author_id=author_instance, book_title="Anne of Green Gables (Anne of Green Gables, #1)", description='This heartwarming story has beckoned generations of readers into the special world of Green Gables, an old-fashioned farm outside a town called Avonlea. Anne Shirley, an eleven-year-old orphan, has arrived in this verdant corner of Prince Edward Island only to discover that the Cuthberts—elderly Matthew and his stern sister, Marilla—want to adopt a boy, not a feisty redheaded girl. But before they can send her back, Anne—who simply must have more scope for her imagination and a real home—wins them over completely. A much-loved classic that explores all the vulnerability, expectations, and dreams of a child growing up, Anne of Green Gables is also a wonderful portrait of a time, a place, a family… and, most of all, love. WITH AN AFTERWORD BY JENNIFER LEE CARELL', avg_rating=4.3, num_rating=918700, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1615094578i/8127.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Alexandre Dumas", "username": "alexandredumas", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("alexandredumas")
print("The Count of Monte Cristo")
book = Book(author_id=author_instance, book_title="The Count of Monte Cristo", description='Thrown in prison for a crime he has not committed, Edmond Dantès is confined to the grim fortress of If. There he learns of a great hoard of treasure hidden on the Isle of Monte Cristo and he becomes determined not only to escape, but also to unearth the treasure and use it to plot the destruction of the three men responsible for his incarceration. Dumas’ epic tale of suffering and retribution, inspired by a real-life case of wrongful imprisonment, was a huge popular success when it was first serialized in the 1840s.Robin Buss’s lively English translation is complete and unabridged, and remains faithful to the style of Dumas’s original. This edition includes an introduction, explanatory notes and suggestions for further reading.', avg_rating=4.29, num_rating=867955, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1611834134i/7126.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Orson Scott Card", "username": "orsonscottcard", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("orsonscottcard")
print("Ender’s Game (Ender's Saga, #1)")
book = Book(author_id=author_instance, book_title="Ender’s Game (Ender's Saga, #1)", description='Andrew "Ender" Wiggin thinks he is playing computer simulated war games; he is, in fact, engaged in something far more desperate. The result of genetic experimentation, Ender may be the military genius Earth desperately needs in a war against an alien enemy seeking to destroy all human life. The only way to find out is to throw Ender into ever harsher training, to chip away and find the diamond inside, or destroy him utterly. Ender Wiggin is six years old when it begins. He will grow up fast.But Ender is not the only result of the experiment. The war with the Buggers has been raging for a hundred years, and the quest for the perfect general has been underway almost as long. Ender\u0027s two older siblings, Peter and Valentine, are every bit as unusual as he is, but in very different ways. While Peter was too uncontrollably violent, Valentine very nearly lacks the capability for violence altogether. Neither was found suitable for the military\u0027s purpose. But they are driven by their jealousy of Ender, and by their inbred drive for power. Peter seeks to control the political process, to become a ruler. Valentine\u0027s abilities turn more toward the subtle control of the beliefs of commoner and elite alike, through powerfully convincing essays. Hiding their youth and identities behind the anonymity of the computer networks, these two begin working together to shape the destiny of Earth-an Earth that has no future at all if their brother Ender fails.', avg_rating=4.31, num_rating=1309236, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1408303130i/375802.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Maurice Sendak", "username": "mauricesendak", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("mauricesendak")
print("Where the Wild Things Are")
book = Book(author_id=author_instance, book_title="Where the Wild Things Are", description='Max, a wild and naughty boy, is sent to bed without his supper by his exhausted mother. In his room, he imagines sailing far away to a land of Wild Things. Instead of eating him, the Wild Things make Max their king.',
            avg_rating=4.24, num_rating=963323, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1384434560i/19543.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Alice Walker", "username": "alicewalker", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("alicewalker")
print("The Color Purple")
book = Book(author_id=author_instance, book_title="The Color Purple", description='Winner of the Pulitzer Prize and the National Book Award. Alice Walker\u0027s iconic modern classic is now a Penguin Book.A powerful cultural touchstone of modern American literature, The Color Purple depicts the lives of African American women in early twentieth-century rural Georgia. Separated as girls, sisters Celie and Nettie sustain their loyalty to and hope in each other across time, distance and silence. Through a series of letters spanning twenty years, first from Celie to God, then the sisters to each other despite the unknown, the novel draws readers into its rich and memorable portrayals of Celie, Nettie, Shug Avery and Sofia and their experience. The Color Purple broke the silence around domestic and sexual abuse, narrating the lives of women through their pain and struggle, companionship and growth, resilience and bravery. Deeply compassionate and beautifully imagined, Alice Walker\u0027s epic carries readers on a spirit-affirming journey towards redemption and love.', avg_rating=4.26, num_rating=633920, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1572261616l/52892857.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Yann Martel", "username": "yannmartel", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("yannmartel")
print("Life of Pi")
book = Book(author_id=author_instance, book_title="Life of Pi", description='Life of Pi is a fantasy adventure novel by Yann Martel published in 2001. The protagonist, Piscine Molitor "Pi" Patel, a Tamil boy from Pondicherry, explores issues of spirituality and practicality from an early age. He survives 227 days after a shipwreck while stranded on a boat in the Pacific Ocean with a Bengal tiger named Richard Parker.',
            avg_rating=3.93, num_rating=1552035, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1631251689i/4214.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Margaret Atwood", "username": "margaretatwood", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("margaretatwood")
print("The Handmaid’s Tale (The Handmaid's Tale, #1)")
book = Book(author_id=author_instance, book_title="The Handmaid’s Tale (The Handmaid's Tale, #1)", description='Offred is a Handmaid in the Republic of Gilead. She may leave the home of the Commander and his wife once a day to walk to food markets whose signs are now pictures instead of words because women are no longer allowed to read. She must lie on her back once a month and pray that the Commander makes her pregnant, because in an age of declining births, Offred and the other Handmaids are valued only if their ovaries are viable. Offred can remember the years before, when she lived and made love with her husband, Luke; when she played with and protected her daughter; when she had a job, money of her own, and access to knowledge. But all of that is gone now…Funny, unexpected, horrifying, and altogether convincing, The Handmaid\u0027s Tale is at once scathing satire, dire warning, and tour de force.', avg_rating=4.13, num_rating=1891991, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1578028274i/38447.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Ken Kesey", "username": "kenkesey", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("kenkesey")
print("One Flew Over the Cuckoo's Nest")
book = Book(author_id=author_instance, book_title="One Flew Over the Cuckoo's Nest", description='Alternate cover edition of ISBN 9780451163967Tyrannical Nurse Ratched rules her ward in an Oregon State mental hospital with a strict and unbending routine, unopposed by her patients, who remain cowed by mind-numbing medication and the threat of electric shock therapy. But her regime is disrupted by the arrival of McMurphy – the swaggering, fun-loving trickster with a devilish grin who resolves to oppose her rules on behalf of his fellow inmates. His struggle is seen through the eyes of Chief Bromden, a seemingly mute half-Indian patient who understands McMurphy\u0027s heroic attempt to do battle with the powers that keep them imprisoned. Ken Kesey\u0027s extraordinary first novel is an exuberant, ribald and devastatingly honest portrayal of the boundaries between sanity and madness.', avg_rating=4.2, num_rating=705198, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1516211014i/332613.jpg")
book.save()

author_form = AuthorRegistrationForm({"full_name": "Mary Wollstonecraft Shelley",
                                     "username": "marywollstonecraftshelley", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("marywollstonecraftshelley")
print("Frankenstein: The 1818 Text")
book = Book(author_id=author_instance, book_title="Frankenstein: The 1818 Text", description='This is a previously-published edition of ISBN 9780143131847. Mary Shelley\u0027s seminal novel of the scientist whose creation becomes a monster. This edition is the original 1818 text, which preserves the hard-hitting and politically charged aspects of Shelley\u0027s original writing, as well as her unflinching wit and strong female voice. This edition also includes a new introduction and suggestions for further reading by author and Shelley expert Charlotte Gordon, literary excerpts and reviews selected by Gordon and a chronology and essay by preeminent Shelley scholar Charles E. Robinson.',
            avg_rating=3.85, num_rating=1470152, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1631088473i/35031085.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Daniel Keyes", "username": "danielkeyes", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("danielkeyes")
print("Flowers for Algernon")
book = Book(author_id=author_instance, book_title="Flowers for Algernon", description='The story of a mentally disabled man whose experimental quest for intelligence mirrors that of Algernon, an extraordinary lab mouse. In diary entries, Charlie tells how a brain operation increases his IQ and changes his life. As the experimental procedure takes effect, Charlie\u0027s intelligence expands until it surpasses that of the doctors who engineered his metamorphosis. The experiment seems to be a scientific breakthrough of paramount importance until Algernon begins his sudden, unexpected deterioration. Will the same happen to Charlie?',
            avg_rating=4.19, num_rating=614176, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1689071681i/18373.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Leo Tolstoy", "username": "leotolstoy", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("leotolstoy")
print("Anna Karenina")
book = Book(author_id=author_instance, book_title="Anna Karenina", description='Acclaimed by many as the world\u0027s greatest novel, Anna Karenina provides a vast panorama of contemporary life in Russia and of humanity in general. In it Tolstoy uses his intense imaginative insight to create some of the most memorable characters in all of literature. Anna is a sophisticated woman who abandons her empty existence as the wife of Karenin and turns to Count Vronsky to fulfil her passionate nature - with tragic consequences. Levin is a reflection of Tolstoy himself, often expressing the author\u0027s own views and convictions.Throughout, Tolstoy points no moral, merely inviting us not to judge but to watch. As Rosemary Edmonds comments, \u0027He leaves the shifting patterns of the kaleidoscope to bring home the meaning of the brooding words following the title, \u0027Vengeance is mine, and I will repay.', avg_rating=4.08, num_rating=799913, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1546091617i/15823480.jpg")
book.save()
print("War and Peace")
book = Book(author_id=author_instance, book_title="War and Peace", description='In Russia\u0027s struggle with Napoleon, Tolstoy saw a tragedy that involved all mankind. War and Peace broadly focuses on Napoleon’s invasion of Russia in 1812 and follows three of the most well-known characters in literature: Pierre Bezukhov, the illegitimate son of a count who is fighting for his inheritance and yearning for spiritual fulfillment; Prince Andrei Bolkonsky, who leaves his family behind to fight in the war against Napoleon; and Natasha Rostov, the beautiful young daughter of a nobleman who intrigues both men.As Napoleon’s army invades, Tolstoy brilliantly follows characters from diverse backgrounds—peasants and nobility, civilians and soldiers—as they struggle with the problems unique to their era, their history, and their culture. And as the novel progresses, these characters transcend their specificity, becoming some of the most moving—and human—figures in world literature.Tolstoy gave his personal approval to this translation, published here in a new single volume edition, which includes an introduction by Henry Gifford, and Tolstoy\u0027s important essay `Some Words about War and Peace\u0027.', avg_rating=4.15, num_rating=310975, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1413215930i/656.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Mitch Albom", "username": "mitchalbom", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("mitchalbom")
print("Tuesdays with Morrie")
book = Book(author_id=author_instance, book_title="Tuesdays with Morrie", description='Maybe it was a grandparent, or a teacher or a colleague. Someone older, patient and wise, who understood you when you were young and searching, and gave you sound advice to help you make your way through it. For Mitch Albom, that person was Morrie Schwartz, his college professor from nearly twenty years ago.Maybe, like Mitch, you lost track of this mentor as you made your way, and the insights faded. Wouldn\u0027t you like to see that person again, ask the bigger questions that still haunt you? Mitch Albom had that second chance. He rediscovered Morrie in the last months of the older man\u0027s life. Knowing he was dying of ALS - or motor neurone disease - Mitch visited Morrie in his study every Tuesday, just as they used to back in college. Their rekindled relationship turned into one final \u0027class\u0027: lessons in how to live.', avg_rating=4.16, num_rating=954913, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1423763749i/6900.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "A.A. Milne", "username": "a.a.milne", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("a.a.milne")
print("Winnie-the-Pooh (Winnie-the-Pooh #1)")
book = Book(author_id=author_instance, book_title="Winnie-the-Pooh (Winnie-the-Pooh #1)", description='The adventures of Christopher Robin and his friends in which Pooh Bear uses a balloon to get honey, Piglet meets a Heffalump, and Eeyore has a birthday.',
            avg_rating=4.35, num_rating=313861, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1298440130i/99107.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Kurt Vonnegut Jr.", "username": "kurtvonnegutjr.", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("kurtvonnegutjr.")
print("Slaughterhouse-Five")
book = Book(author_id=author_instance, book_title="Slaughterhouse-Five", description='Selected by the Modern Library as one of the 100 best novels of all time, Slaughterhouse-Five, an American classic, is one of the world\u0027s great antiwar books. Centering on the infamous firebombing of Dresden, Billy Pilgrim\u0027s odyssey through time reflects the mythic journey of our own fractured lives as we search for meaning in what we fear most.',
            avg_rating=4.09, num_rating=1302806, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1440319389i/4981.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Ernest Hemingway", "username": "ernesthemingway", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("ernesthemingway")
print("The Old Man and the Sea")
book = Book(author_id=author_instance, book_title="The Old Man and the Sea", description='Librarian\u0027s note: An alternate cover edition can be found hereThis short novel, already a modern classic, is the superbly told, tragic story of a Cuban fisherman in the Gulf Stream and the giant Marlin he kills and loses—specifically referred to in the citation accompanying the author\u0027s Nobel Prize for literature in 1954.',
            avg_rating=3.8, num_rating=1060714, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1329189714i/2165.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Joseph Heller", "username": "josephheller", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("josephheller")
print("Catch-22")
book = Book(author_id=author_instance, book_title="Catch-22", description='Fifty years after its original publication, Catch-22 remains a cornerstone of American literature and one of the funniest—and most celebrated—books of all time. In recent years it has been named to “best novels” lists by Time, Newsweek, the Modern Library, and the London Observer.Set in Italy during World War II, this is the story of the incomparable, malingering bombardier, Yossarian, a hero who is furious because thousands of people he has never met are trying to kill him. But his real problem is not the enemy—it is his own army, which keeps increasing the number of missions the men must fly to complete their service. Yet if Yossarian makes any attempt to excuse himself from the perilous missions he’s assigned, he’ll be in violation of Catch-22, a hilariously sinister bureaucratic rule: a man is considered insane if he willingly continues to fly dangerous combat missions, but if he makes a formal request to be removed from duty, he is proven sane and therefore ineligible to be relieved.This fiftieth-anniversary edition commemorates Joseph Heller’s masterpiece with a new introduction by Christopher Buckley; a wealth of critical essays and reviews by Norman Mailer, Alfred Kazin, Anthony Burgess, and others; rare papers and photos from Joseph Heller’s personal archive; and much more. Here, at last, is the definitive edition of a classic of world literature.', avg_rating=3.99, num_rating=804276, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1463157317i/168668.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Nathaniel Hawthorne", "username": "nathanielhawthorne", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("nathanielhawthorne")
print("The Scarlet Letter")
book = Book(author_id=author_instance, book_title="The Scarlet Letter", description='Set in 17th-century Puritan Boston, Massachusetts, during the years 1642 to 1649, it tells the story of Hester Prynne, who conceives a daughter through an affair and will not reveal her lover’s identity. The scarlet letter A (for adultery) she has to wear on her clothes, along with her public shaming, is her punishment for her sin and her secrecy. She struggles to create a new life of repentance and dignity. Throughout the book, Hawthorne explores themes of legalism, sin, and guilt.',
            avg_rating=3.43, num_rating=825467, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1404810944i/12296.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Stephenie Meyer", "username": "stepheniemeyer", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("stepheniemeyer")
print("Twilight (The Twilight Saga, #1)")
book = Book(author_id=author_instance, book_title="Twilight (The Twilight Saga, #1)", description='About three things I was absolutely positive.First, Edward was a vampire.Second, there was a part of him—and I didn\u0027t know how dominant that part might be—that thirsted for my blood.And third, I was unconditionally and irrevocably in love with him.Deeply seductive and extraordinarily suspenseful, Twilight is a love story with bite.',
            avg_rating=3.64, num_rating=6158643, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1361039443i/41865.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Vladimir Nabokov", "username": "vladimirnabokov", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("vladimirnabokov")
print("Lolita")
book = Book(author_id=author_instance, book_title="Lolita", description='Librarian\u0027s note: Alternate cover edition of ISBN 9780141182537.Humbert Humbert - scholar, aesthete and romantic - has fallen completely and utterly in love with Dolores Haze, his landlady\u0027s gum-snapping, silky skinned twelve-year-old daughter. Reluctantly agreeing to marry Mrs Haze just to be close to Lolita, Humbert suffers greatly in the pursuit of romance; but when Lo herself starts looking for attention elsewhere, he will carry her off on a desperate cross-country misadventure, all in the name of Love. Hilarious, flamboyant, heart-breaking and full of ingenious word play, Lolita is an immaculate, unforgettable masterpiece of obsession, delusion and lust.',
            avg_rating=3.88, num_rating=794964, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1377756377i/7604.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Franz Kafka", "username": "franzkafka", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("franzkafka")
print("The Metamorphosis")
book = Book(author_id=author_instance, book_title="The Metamorphosis", description='Alternate cover edition of ISBN 0553213695 / 9780553213690"As Gregor Samsa awoke one morning from uneasy dreams he found himself transformed in his bed into a gigantic insect. He was laying on his hard, as it were armor-plated, back and when he lifted his head a little he could see his domelike brown belly divided into stiff arched segments on top of which the bed quilt could hardly keep in position and was about to slide off completely. His numerous legs, which were pitifully thin compared to the rest of his bulk, waved helplessly before his eyes." With it\u0027s startling, bizarre, yet surprisingly funny first opening, Kafka begins his masterpiece, The Metamorphosis. It is the story of a young man who, transformed overnight into a giant beetle-like insect, becomes an object of disgrace to his family, an outsider in his own home, a quintessentially alienated man. A harrowing—though absurdly comic—meditation on human feelings of inadequacy, guilt, and isolation, The Metamorphosis has taken its place as one of the most widely read and influential works of twentieth-century fiction. As W.H. Auden wrote, "Kafka is important to us because his predicament is the predicament of modern man.', avg_rating=3.85, num_rating=918431, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1646444605i/485894.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Audrey Niffenegger", "username": "audreyniffenegger", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("audreyniffenegger")
print("The Time Traveler's Wife")
book = Book(author_id=author_instance, book_title="The Time Traveler's Wife", description='This is the extraordinary love story of Clare and Henry, who met when Clare was six and Henry was thirty-six, and were married when Clare was twenty-two and Henry was thirty. Impossible but true, because Henry suffers from a rare condition where his genetic clock periodically resets and he finds himself pulled suddenly into his past or future. In the face of this force they can neither prevent nor control, Henry and Clare\u0027s struggle to lead normal lives is both intensely moving and entirely unforgettable.',
            avg_rating=3.99, num_rating=1736216, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1380660571i/18619684.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Hermann Hesse", "username": "hermannhesse", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("hermannhesse")
print("Siddhartha")
book = Book(author_id=author_instance, book_title="Siddhartha", description='Herman Hesse\u0027s classic novel has delighted, inspired, and influenced generations of readers, writers, and thinkers. In this story of a wealthy Indian Brahmin who casts off a life of privilege to seek spiritual fulfillment. Hesse synthesizes disparate philosophies--Eastern religions, Jungian archetypes, Western individualism--into a unique vision of life as expressed through one man\u0027s search for true meaning.',
            avg_rating=4.06, num_rating=720467, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1629378189i/52036.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Albert Camus", "username": "albertcamus", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("albertcamus")
print("The Stranger")
book = Book(author_id=author_instance, book_title="The Stranger", description='Published in 1942 by French author Albert Camus, The Stranger has long been considered a classic of twentieth-century literature. Le Monde ranks it as number one on its "100 Books of the Century" list. Through this story of an ordinary man unwittingly drawn into a senseless murder on a sundrenched Algerian beach, Camus explores what he termed "the nakedness of man faced with the absurd.',
            avg_rating=4.01, num_rating=960905, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1590930002i/49552.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Margaret Wise Brown", "username": "margaretwisebrown", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("margaretwisebrown")
print("Goodnight Moon")
book = Book(author_id=author_instance, book_title="Goodnight Moon", description='In a great green room, tucked away in bed, is a little bunny. "Goodnight room, goodnight moon." And to all the familiar things in the softly lit room -- to the picture of the three little bears sitting on chairs, to the clocks and his socks, to the mittens and the kittens, to everything one by one -- the little bunny says goodnight.In this classic of children\u0027s literature, beloved by generations of readers and listeners, the quiet poetry of the words and the gentle, lulling illustrations combine to make a perfect book for the end of the day.',
            avg_rating=4.3, num_rating=358773, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1439223893i/32929.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Betty  Smith", "username": "bettysmith", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("bettysmith")
print("A Tree Grows in Brooklyn")
book = Book(author_id=author_instance, book_title="A Tree Grows in Brooklyn", description='The beloved American classic about a young girl\u0027s coming-of-age at the turn of the century, Betty Smith\u0027s A Tree Grows in Brooklyn is a poignant and moving tale filled with compassion and cruelty, laughter and heartache, crowded with life and people and incident. The story of young, sensitive, and idealistic Francie Nolan and her bittersweet formative years in the slums of Williamsburg has enchanted and inspired millions of readers for more than sixty years. By turns overwhelming, sublime, heartbreaking, and uplifting, the daily experiences of the unforgettable Nolans are raw with honesty and tenderly threaded with family connectedness -- in a work of literary art that brilliantly captures a unique time and place as well as incredibly rich moments of universal experience.', avg_rating=4.29, num_rating=442856, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1327883484i/14891.jpg")
book.save()

author_form = AuthorRegistrationForm({"full_name": "Laura Ingalls Wilder",
                                     "username": "lauraingallswilder", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("lauraingallswilder")
print("The Little House Collection (Little House, #1-9)")
book = Book(author_id=author_instance, book_title="The Little House Collection (Little House, #1-9)", description='This nine-book paperback box set of the classic series features the classic black-and-white artwork from Garth Williams.The nine books in the timeless Little House series tell the story of Laura’s real childhood as an American pioneer, and are cherished by readers of all generations. They offer a unique glimpse into life on the American frontier, and tell the heartwarming, unforgettable story of a loving family.Little House in the Big WoodsMeet the Ingalls family—Laura, Ma, Pa, Mary, and baby Carrie, who all live in a cozy log cabin in the big woods of Wisconsin in the 1870s. Though many of their neighbors are wolves and panthers and bears, the woods feel like home, thanks to Ma’s homemade cheese and butter and the joyful sounds of Pa’s fiddle.Farmer BoyAs Laura Ingalls is growing up in a little house in Kansas, Almanzo Wilder lives on a big farm in New York. He and his brothers and sisters work hard from dawn to supper to help keep their family farm running. Almanzo wishes for just one thing—his very own horse—but he must prove that he is ready for such a big responsibility.Little House on the PrairieWhen Pa decides to sell the log house in the woods, the family packs up and moves from Wisconsin to Kansas, where Pa builds them their little house on the prairie! Living on the farm is different from living in the woods, but Laura and her family are kept busy and are happy with the promise of their new life on the prairie.On the Banks of Plum CreekThe Ingalls family lives in a sod house beside Plum Creek in Minnesota until Pa builds them a new house made of sawed lumber. The money for the lumber will come from their first wheat crop. But then, just before the wheat is ready to harvest, a strange glittering cloud fills the sky, blocking out the sun. Millions of grasshoppers cover the field and everything on the farm, and by the end of a week, there is no wheat crop left.By the Shores of Silver LakePa Ingalls heads west to the unsettled wilderness of the Dakota Territory. When Ma, Mary, Laura, Carrie, and baby Grace join him, they become the first settlers in the town of De Smet. Pa starts work on the first building of the brand new town, located on the shores of Silver Lake. The Long WinterThe first terrible storm comes to the barren prairie in October. Then it snows almost without stopping until April. With snow piled as high as the rooftops, it’s impossible for trains to deliver supplies, and the townspeople, including Laura and her family, are starving. Young Almanzo Wilder, who has settled in the town, risks his life to save the town.Little Town on the PrairieDe Smet is rejuvenated with the beginning of spring. But in addition to the parties, socials, and “literaries,” work must continue. Laura spends many hours sewing shirts to help Ma and Pa get enough money to send Mary to a college for the blind. But in the evenings, Laura makes time for a new caller, Almanzo Wilder.These Happy Golden YearsLaura must continue to earn money to keep Mary in her college for the blind, so she gets a job as a teacher. It’s not easy, and for the first time she’s living away from home. But it gets a little better every Friday, when Almanzo picks Laura up to take her back home for the weekend. Though Laura is still young, she and Almanzo are officially courting, and she knows that this is a time for new beginnings.The First Four YearsLaura Ingalls and Almanzo Wilder have just been married! They move to a small prairie homestead to start their lives together. But each year brings new challenges—storms, sickness, fire, and unpaid debts. These first four years call for courage, strength, and a great deal of determination. And through it all, Laura and Almanzo still have their love, which only grows when baby Rose arrives.', avg_rating=4.35, num_rating=150166, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1577932823i/114345.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Anthony Burgess", "username": "anthonyburgess", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("anthonyburgess")
print("A Clockwork Orange")
book = Book(author_id=author_instance, book_title="A Clockwork Orange", description='In Anthony Burgess\u0027s influential nightmare vision of the future, criminals take over after dark. Teen gang leader Alex narrates in fantastically inventive slang that echoes the violent intensity of youth rebelling against society. Dazzling and transgressive, A Clockwork Orange is a frightening fable about good and evil and the meaning of human freedom. This edition includes the controversial last chapter not published in the first edition, and Burgess’s introduction, “A Clockwork Orange Resucked.”',
            avg_rating=4, num_rating=681585, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1549260060i/41817486.jpg")
book.save()

author_form = AuthorRegistrationForm({"full_name": "Erich Maria Remarque",
                                     "username": "erichmariaremarque", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("erichmariaremarque")
print("All Quiet on the Western Front")
book = Book(author_id=author_instance, book_title="All Quiet on the Western Front", description='One by one the boys begin to fall…In 1914 a room full of German schoolboys, fresh-faced and idealistic, are goaded by their schoolmaster to troop off to the ‘glorious war’. With the fire and patriotism of youth they sign up. What follows is the moving story of a young ‘unknown soldier’ experiencing the horror and disillusionment of life in the trenches.',
            avg_rating=4.05, num_rating=427431, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1632027397i/355697.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Stephen King", "username": "stephenking", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("stephenking")
print("The Stand")
book = Book(author_id=author_instance, book_title="The Stand", description='First came the days of the plague. Then came the dreams. Dark dreams that warned of the coming of the dark man. The apostate of death, his worn-down boot heels tramping the night roads. The warlord of the charnel house and Prince of Evil. His time is at hand. His empire grows in the west and the Apocalypse looms.For hundreds of thousands of fans who read The Stand in its original version and wanted more, this new edition is Stephen King\u0027s gift. And those who are listening to The Stand for the first time will discover a triumphant and eerily plausible work of the imagination that takes on the issues that will determine our survival.',
            avg_rating=4.34, num_rating=722312, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1213131305i/149267.jpg")
book.save()

author_form = AuthorRegistrationForm({"full_name": "Miguel de Cervantes Saavedra",
                                     "username": "migueldecervantessaavedra", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("migueldecervantessaavedra")
print("Don Quixote")
book = Book(author_id=author_instance, book_title="Don Quixote", description='Don Quixote has become so entranced by reading chivalric romances that he determines to become a knight-errant himself. In the company of his faithful squire, Sancho Panza, his exploits blossom in all sorts of wonderful ways. While Quixote\u0027s fancy often leads him astray—he tilts at windmills, imagining them to be giants—Sancho acquires cunning and a certain sagacity. Sane madman and wise fool, they roam the world together, and together they have haunted readers\u0027 imaginations for nearly four hundred years.With its experimental form and literary playfulness, Don Quixote has been generally recognized as the first modern novel. The book has been enormously influential on a host of writers, from Fielding and Sterne to Flaubert, Dickens, Melville, and Faulkner, who reread it once a year, "just as some people read the Bible.', avg_rating=3.89, num_rating=254292, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1546112331i/3836.jpg")
book.save()

author_form = AuthorRegistrationForm({"full_name": "Harriet Beecher Stowe",
                                     "username": "harrietbeecherstowe", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("harrietbeecherstowe")
print("Uncle Tom's Cabin")
book = Book(author_id=author_instance, book_title="Uncle Tom's Cabin", description='The narrative drive of Stowe\u0027s classic novel is often overlooked in the heat of the controversies surrounding its anti-slavery sentiments. In fact, it is a compelling adventure story with richly drawn characters and has earned a place in both literary and American history. Stowe\u0027s religious beliefs show up in the novel\u0027s final, overarching theme—the exploration of the nature of Christianity and how Christian theology is fundamentally incompatible with slavery.',
            avg_rating=3.9, num_rating=219238, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1414349231i/46787.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Ayn Rand", "username": "aynrand", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("aynrand")
print("Atlas Shrugged")
book = Book(author_id=author_instance, book_title="Atlas Shrugged", description='This is the story of a man who said that he would stop the motor of the world and did. Was he a destroyer or the greatest of liberators?Why did he have to fight his battle, not against his enemies, but against those who needed him most, and his hardest battle against the woman he loved? What is the world’s motor — and the motive power of every man? You will know the answer to these questions when you discover the reason behind the baffling events that play havoc with the lives of the characters in this story. Tremendous in its scope, this novel presents an astounding panorama of human life — from the productive genius who becomes a worthless playboy — to the great steel industrialist who does not know that he is working for his own destruction — to the philosopher who becomes a pirate — to the composer who gives up his career on the night of his triumph — to the woman who runs a transcontinental railroad — to the lowest track worker in her Terminal tunnels. You must be prepared, when you read this novel, to check every premise at the root of your convictions.This is a mystery story, not about the murder — and rebirth — of man’s spirit. It is a philosophical revolution, told in the form of an action thriller of violent events, a ruthlessly brilliant plot structure and an irresistible suspense. Do you say this is impossible? Well, that is the first of your premises to check.', avg_rating=3.69, num_rating=380464, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1405868167i/662.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Barbara Kingsolver", "username": "barbarakingsolver", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("barbarakingsolver")
print("The Poisonwood Bible")
book = Book(author_id=author_instance, book_title="The Poisonwood Bible", description='The Poisonwood Bible is a story told by the wife and four daughters of Nathan Price, a fierce, evangelical Baptist who takes his family and mission to the Belgian Congo in 1959. They carry with them everything they believe they will need from home, but soon find that all of it -- from garden seeds to Scripture -- is calamitously transformed on African soil. What follows is a suspenseful epic of one family\u0027s tragic undoing and remarkable reconstruction over the course of three decades in postcolonial Africa.',
            avg_rating=4.09, num_rating=716880, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1644073807i/7244.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Maya Angelou", "username": "mayaangelou", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("mayaangelou")
print("I Know Why the Caged Bird Sings (Maya Angelou's Autobiography, #1)")
book = Book(author_id=author_instance, book_title="I Know Why the Caged Bird Sings (Maya Angelou's Autobiography, #1)", description='Maya Angelou’s debut memoir is a modern American classic beloved worldwide. Her life story is told in the documentary film And Still I Rise, as seen on PBS’s American Masters.Here is a book as joyous and painful, as mysterious and memorable, as childhood itself. I Know Why the Caged Bird Sings captures the longing of lonely children, the brute insult of bigotry, and the wonder of words that can make the world right. Maya Angelou’s debut memoir is a modern American classic beloved worldwide. Sent by their mother to live with their devout, self-sufficient grandmother in a small Southern town, Maya and her brother, Bailey, endure the ache of abandonment and the prejudice of the local “powhitetrash.” At eight years old and back at her mother’s side in St. Louis, Maya is attacked by a man many times her age—and has to live with the consequences for a lifetime. Years later, in San Francisco, Maya learns that love for herself, the kindness of others, her own strong spirit, and the ideas of great authors (“I met and fell in love with William Shakespeare”) will allow her to be free instead of imprisoned. Poetic and powerful, I Know Why the Caged Bird Sings will touch hearts and change minds for as long as people read.', avg_rating=4.28, num_rating=501912, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1327957927i/13214.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Joseph Smith Jr.", "username": "josephsmithjr.", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("josephsmithjr.")
print("The Book of Mormon: Another Testament of Jesus Christ")
book = Book(author_id=author_instance, book_title="The Book of Mormon: Another Testament of Jesus Christ", description='This work has been selected by scholars as being culturally important, and is part of the knowledge base of civilization as we know it. This work was reproduced from the original artifact, and remains as true to the original work as possible. Therefore, you will see the original copyright references, library stamps (as most of these works have been housed in our most important libraries around the world), and other notations in the work.This work is in the public domain in the United States of America, and possibly other nations. Within the United States, you may freely copy and distribute this work, as no entity (individual or corporate) has a copyright on the body of the work.As a reproduction of a historical artifact, this work may contain missing or blurred pages, poor pictures, errant marks, etc. Scholars believe, and we concur, that this work is important enough to be preserved, reproduced, and made generally available to the public. We appreciate your support of the preservation process, and thank you for being an important part of keeping this knowledge alive and relevant.', avg_rating=4.26, num_rating=83595, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1327389004i/323355.jpg")
book.save()

author_form = AuthorRegistrationForm(
    {"full_name": "Herman Melville", "username": "hermanmelville", "password1": "halo123", "password2": "halo123"})
author_instance = author_form.save()
print("hermanmelville")
print("Moby-Dick or, the Whale")
book = Book(author_id=author_instance, book_title="Moby-Dick or, the Whale", description='It is the horrible texture of a fabric that should be woven of ships\u0027 cables and hawsers. A Polar wind blows through it, and birds of prey hover over it." So Melville wrote of his masterpiece, one of the greatest works of imagination in literary history. In part, Moby-Dick is the story of an eerily compelling madman pursuing an unholy war against a creature as vast and dangerous and unknowable as the sea itself. But more than just a novel of adventure, more than an encyclopaedia of whaling lore and legend, the book can be seen as part of its author\u0027s lifelong meditation on America. Written with wonderfully redemptive humour, Moby-Dick is also a profound inquiry into character, faith, and the nature of perception.This edition of Moby-Dick, which reproduces the definitive text of the novel, includes invaluable explanatory notes, along with maps, illustrations, and a glossary of nautical terms.', avg_rating=3.53, num_rating=535225, book_cover_link="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1327940656i/153747.jpg")
book.save()
