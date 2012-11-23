/* auto-generated by genmsg_cpp from /home/tjay/ros/ros/naoExpmnt/msg/Motion.msg.  Do not edit! */
#ifndef NAOEXPMNT_MOTION_H
#define NAOEXPMNT_MOTION_H

#include <string>
#include <vector>
#include "ros/message.h"
#include "ros/time.h"

namespace naoExpmnt
{

//! \htmlinclude Motion.msg.html

class Motion : public ros::Message
{
public:
  typedef boost::shared_ptr<Motion> Ptr;
  typedef boost::shared_ptr<Motion const> ConstPtr;

  typedef uint8_t _forward_type;
  typedef uint8_t _left_type;
  typedef uint8_t _right_type;
  typedef uint8_t _stand_type;

  uint8_t forward;
  uint8_t left;
  uint8_t right;
  uint8_t stand;

  Motion() : ros::Message(),
    forward(0),
    left(0),
    right(0),
    stand(0)
  {
  }
  Motion(const Motion &copy) : ros::Message(),
    forward(copy.forward),
    left(copy.left),
    right(copy.right),
    stand(copy.stand)
  {
    (void)copy;
  }
  Motion &operator =(const Motion &copy)
  {
    if (this == &copy)
      return *this;
    forward = copy.forward;
    left = copy.left;
    right = copy.right;
    stand = copy.stand;
    return *this;
  }
  virtual ~Motion() 
  {
  }
  inline static std::string __s_getDataType() { return std::string("naoExpmnt/Motion"); }
  inline static std::string __s_getMD5Sum() { return std::string("610c37bd2a189fd95f9d3aad2177aef9"); }
  inline static std::string __s_getMessageDefinition()
  {
    return std::string(
    "uint8 forward\n"
    "uint8 left\n"
    "uint8 right\n"
    "uint8 stand\n"
    "\n"
    "\n"
    );
  }
  inline virtual const std::string __getDataType() const { return __s_getDataType(); }
  inline virtual const std::string __getMD5Sum() const { return __s_getMD5Sum(); }
  inline virtual const std::string __getMessageDefinition() const { return __s_getMessageDefinition(); }
  inline uint32_t serializationLength() const
  {
    unsigned __l = 0;
    __l += 1; // forward
    __l += 1; // left
    __l += 1; // right
    __l += 1; // stand
    return __l;
  }
  virtual uint8_t *serialize(uint8_t *write_ptr, uint32_t seq) const
  {
    SROS_SERIALIZE_PRIMITIVE(write_ptr, forward);
    SROS_SERIALIZE_PRIMITIVE(write_ptr, left);
    SROS_SERIALIZE_PRIMITIVE(write_ptr, right);
    SROS_SERIALIZE_PRIMITIVE(write_ptr, stand);
    return write_ptr;
  }
  virtual uint8_t *deserialize(uint8_t *read_ptr)
  {
    SROS_DESERIALIZE_PRIMITIVE(read_ptr, forward);
    SROS_DESERIALIZE_PRIMITIVE(read_ptr, left);
    SROS_DESERIALIZE_PRIMITIVE(read_ptr, right);
    SROS_DESERIALIZE_PRIMITIVE(read_ptr, stand);
    return read_ptr;
  }
};

typedef boost::shared_ptr<Motion> MotionPtr;
typedef boost::shared_ptr<Motion const> MotionConstPtr;


}

#endif
