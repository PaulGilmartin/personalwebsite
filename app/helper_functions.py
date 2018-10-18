from app import create_app, db
from app.main.models import Paper, Photograph, Painting, Project
from config import Config


class_map = {cls.__name__: cls for cls in (Paper, Photograph, Painting, Project)}


def app_context(config_class=Config):
    app = create_app(config_class)
    return app.app_context()


def create_model_item(class_name, **kwargs):
    with app_context():
        item = class_map[class_name](**kwargs)
    return item


def commit_item(item, database=None, config_class=Config):
    with app_context(config_class):
        database = database or db
        database.session.add(item)
        database.session.commit()


def get_all_items_of_type(model_name, config_class=Config):
    with app_context(config_class):
        model_cls = class_map[model_name]
        all_items = model_cls.query.all()
    return all_items


def delete_item(item, database=None, config_class=Config):
    with app_context(config_class):
        database = database or db
        database.session.delete(item)
        database.session.commit()


def build_records(database=None, config_class=Config):
    with app_context(config_class):
        database = database or db

        # kgPhoto = create_model_item('Photograph', content_path='../static/kelvinbridgePhotograph.JPG',
        #                             title='Kelvinbridge', subject='Glasgow')
        # kgPainting = create_model_item('Painting', content_path='../static/kelvinBridgePainting.png',
        #                                title='Kelvinbridge', subject='Glasgow', photograph=kgPhoto)
        #
        # wPhoto = create_model_item('Photograph', content_path='../static/westPrincesStreetPhotograph.JPG',
        #                            title='West Princes Street', subject='Glasgow')
        # wPainting = create_model_item('Painting', content_path='../static/westPrincesStreetPainting.png',
        #                               title='West Princes Street', subject='Glasgow', photograph=wPhoto)

        maryhill = create_model_item('Photograph', content_path='../static/maryhill.jpg',
                                      title='Maryhill', subject='Glasgow')
        queenStreet = create_model_item('Photograph', content_path='../static/queenStreet.jpg',
                                        title='Queen Street Station', subject='Glasgow')
        chippy = create_model_item('Photograph', content_path='../static/chippy.jpg',
                                    title='Chippy, Alexandra Parade', subject='Glasgow')
        kelvin = create_model_item('Photograph', content_path='../static/theKelvin.jpg',
                                    title='The Kelvin', subject='Glasgow')

        doublet = create_model_item('Photograph', content_path='../static/theDoublet.jpg',
                                    title='The Doublet, Woodlands', subject='Pub')
        louden = create_model_item('Photograph', content_path='../static/theLoudenTavern.jpg',
                                    title='The Louden Tavern, Duke Street', subject='Pub')

        quantum = create_model_item('Paper',
                                    content_path='https://www.sciencedirect.com/science/article/pii/S0021869316000673',
                                    title='Quantum homogeneous spaces of connected Hopf algebras',
                                    coauthors='Ken Brown',
                                    abstract="""Let H be a connected Hopf k-algebra of finite Gel'fand–Kirillov dimension
                                                over an algebraically closed field k of characteristic 0. The objects of
                                                study in this paper are the left or right coideal subalgebras T of H.
                                                They are shown to be deformations of commutative polynomial k-algebras.
                                                A number of well-known homological and other properties follow immediately
                                                from this fact. Further properties are described, examples are considered,
                                                invariants are constructed and a number of open questions are 
                                                listed.""")

        graded = create_model_item('Paper',
                                    content_path='https://arxiv.org/abs/1601.06687',
                                    title='Connected (graded) Hopf algebras',
                                    coauthors='Ken Brown, James Zhang',
                                    abstract="""We study algebraic and homological properties of two classes of infinite
                                     dimensional Hopf algebras over an algebraically closed field k of characteristic zero.
                                      The first class consists of those Hopf k-algebras that are connected graded as
                                       algebras, and the second class are those Hopf k-algebras that are connected as 
                                       coalgebras. For many but not all of the results presented here, the Hopf algebras
                                        are assumed to have finite Gel'fand-Kirillov dimension. It is shown that if the
                                         Hopf algebra H is a connected graded algebra of finite Gel'fand-Kirillov
                                          dimension n, then H is a noetherian domain which is Cohen-Macaulay, 
                                          Artin-Schelter regular and Auslander regular of global dimension n. 
                                          It has S^2 = Id_H, and is Calabi-Yau. Detailed information is also provided
                                           about the Hilbert series of H. Our results leave open the possibility that 
                                           the first class of algebras is (properly) contained in the second. For this 
                                           second class, the Hopf k-algebras of finite Gel'fand-Kirillov dimension n 
                                           with connected coalgebra, the underlying coalgebra is shown to be 
                                           Artin-Schelter regular of global dimension n. Both these classes of Hopf
                                            algebra share many features in common with enveloping algebras of finite 
                                            dimensional Lie algebras. For example, an algebra in either of these classes
                                             satisfies a polynomial identity only if it is a commutative polynomial 
                                             algebra. Nevertheless, we construct, as one of our main results, an
                                              example of a Hopf k-algebra H of Gel'fand-Kirillov dimension 5, which is 
                                              connected graded as an algebra and connected as a coalgebra, but is not 
                                              isomorphic as an algebra to U(g) for any Lie algebra g.""")

        finite = create_model_item('Paper',
                                    content_path='http://pjm.ppu.edu/vol_3_3/3.pdf',
                                    title='Hopf algebras under finiteness conditions',
                                    coauthors='Ken Brown',
                                    abstract="""This is a brief survey of some recent developments in the study of infinite dimensional
                                                Hopf algebras which are either noetherian or have finite Gelfand-Kirillov dimension. A
                                                number of open questions are listed.""")

        antipode = create_model_item('Paper',
                                    content_path='https://arxiv.org/abs/1611.03480',
                                    title='A note on the order of the antipode of a pointed Hopf algebra',
                                    abstract="""Let k be a field and let H denote a pointed Hopf k-algebra with 
                                    antipode S. We are interested in determining the order of S. Building on the
                                     work done by Taft and Wilson [7], we define an invariant for H, denoted mH, 
                                     and prove that the value of this invariant is connected to the order of S. 
                                     In the case where chark=0, it is shown that if S has finite order then it is 
                                     either the identity or has order 2mH. If in addition H is assumed to be 
                                     coradically graded, it is shown that the order of S is finite if and only
                                      if mH is finite. We also consider the case where chark=p>0, generalising 
                                      the results of [7] to the infinite-dimensional setting.""")

        for i in [maryhill, queenStreet, chippy, kelvin, doublet, louden, quantum, finite, graded, antipode]:
            commit_item(i)
