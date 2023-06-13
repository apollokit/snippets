// the actual docs: https://eigen.tuxfamily.org/dox/group__TutorialMatrixClass.html
// https://www.cc.gatech.edu/classes/AY2016/cs4496_spring/Eigen.html

#include <sstream>

#include <Eigen/Dense>

static std::string toString(const Eigen::MatrixXd& mat){
    std::stringstream ss;
    ss << mat;
    return ss.str();
}

static void test(uint64_t simTimeNanos, Eigen::Vector3d r_I)
{

    // printf("GravBodyData::computeGravityInertial: %s: %.15f %.15f %.15f");
    // printf("Firing thruster");
    // printf("GravBodyData::computeGravityInertial: ri %s\n", toString(r_I).c_str());

    // better
    printf("GravBodyData::computeGravityInertial: simTimeNanos %d\n", simTimeNanos);
    printf("GravBodyData::computeGravityInertial: ri [%.15f, %.15f, %.15f]\n", r_I[0], r_I[1], r_I[2]);


    Eigen::Matrix3d dcm_PfixN = Eigen::Map<Eigen::Matrix3d>
        (&(this->localPlanet.J20002Pfix[0][0]), 3, 3);
    printf("GravBodyData::computeGravityInertial: dcm_PfixN \n\t[%.15f, %.15f, %.15f]\n\t[%.15f, %.15f, %.15f]\n\t[%.15f, %.15f, %.15f]\n", 
        dcm_PfixN.coeff(0,0), dcm_PfixN.coeff(0,1), dcm_PfixN.coeff(0,2),
        dcm_PfixN.coeff(1,0), dcm_PfixN.coeff(1,1), dcm_PfixN.coeff(1,2),
        dcm_PfixN.coeff(2,0), dcm_PfixN.coeff(2,1), dcm_PfixN.coeff(2,2));

    printf("svIntegratorRK4::integrate: k1 term [%.15f, %.15f, %.15f]\n", itOut->second.state(0), itOut->second.state(1), itOut->second.state(2));


    // from https://eigen.tuxfamily.org/dox/group__TutorialMatrixClass.html
    Eigen::MatrixXd m(2,2);
    m(0,0) = 3;
    m(1,0) = 2.5;
    m(0,1) = -1;
    m(1,1) = m(1,0) + m(0,1);
    std::cout << "Here is the matrix m:\n" << m << std::endl;
    Eigen::VectorXd v(2);
    v(0) = 4;
    v(1) = v(0) - 1;
    std::cout << "Here is the vector v:\n" << v << std::endl;


    Eigen::Matrix3f m;
    m << 1, 2, 3,
         4, 5, 6,
         7, 8, 9;
    std::cout << m;
    std::cout << "2nd Row: " << m.row(1) << std::endl;
    
    Eigen::Vector3f v;
    v = m.row(1);
    std::cout << "v: " << v << std::endl;
    std::cout << m * v;
}